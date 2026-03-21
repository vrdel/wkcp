import os
import shutil
import urllib.parse
from pathlib import Path

from wkcp.utils import MARKDOWN_IMAGE_PATTERN, WIKILINK_IMAGE_PATTERN, VIMWIKI_IMAGE_PATTERN

def extract_all_local_images(content):
    images = []

    # Extract images from all supported formats
    images.extend(MARKDOWN_IMAGE_PATTERN.findall(content))
    images.extend(WIKILINK_IMAGE_PATTERN.findall(content))
    images.extend(VIMWIKI_IMAGE_PATTERN.findall(content))

    # Filter out external URLs, keep only local relative/absolute paths
    local_images = []
    for img in images:
        parsed = urllib.parse.urlparse(img)
        if not parsed.scheme or parsed.scheme == 'file':
            # It's a local path
            if parsed.scheme == 'file':
                # Strip file:// if present (though unlikely in raw wiki source)
                local_images.append(parsed.path)
            else:
                local_images.append(img)

    # Remove duplicates
    return list(set(local_images))


def CopyWikiHandle(args):
    source_file = Path(args.file)
    if not source_file.exists():
        print(f"Error: Source file '{source_file}' does not exist.")
        return

    dest_dir = Path(args.dest)
    try:
        dest_dir.mkdir(parents=True, exist_ok=True)
    except PermissionError:
        print(f"Error: Permission denied when attempting to create destination directory '{dest_dir}'.")
        return
    except Exception as e:
        print(f"Error: Could not create destination directory '{dest_dir}': {e}")
        return

    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()

    local_images = extract_all_local_images(content)

    # We resolve image paths relative to the source wiki file's directory
    source_dir = source_file.parent

    # Copy all referenced local images
    for img_path_str in local_images:
        # If absolute path is used, we might want to just copy it to dest directly,
        # but usually vimwiki links are relative.
        img_path = Path(urllib.parse.unquote(img_path_str))

        # We only copy if it exists relative to the source document or is absolute and exists
        actual_img_path = source_dir / img_path if not img_path.is_absolute() else img_path

        if actual_img_path.exists() and actual_img_path.is_file():
            # If the image link is relative, we preserve its hierarchy inside the dest folder
            # E.g. img_path is 'images/pic.png', dest is '/tmp/dst'. Result: '/tmp/dst/images/pic.png'
            if not img_path.is_absolute():
                target_img_path = dest_dir / img_path
            else:
                target_img_path = dest_dir / actual_img_path.name

            target_img_path.parent.mkdir(parents=True, exist_ok=True)
            try:
                shutil.copy2(actual_img_path, target_img_path)
            except Exception as e:
                print(f"Warning: Failed to copy image {actual_img_path} to {target_img_path}: {e}")
        else:
            print(f"Warning: Referenced image '{actual_img_path}' not found, skipping.")

    # Convert or just copy the main wiki file
    if args.convert_md or args.convert_vimwiki:
        try:
            import pypandoc

            if args.convert_md:
                # Source is vimwiki, dest is md
                dest_file = dest_dir / (source_file.stem + '.md')
                pypandoc.convert_file(
                    str(source_file),
                    'gfm+wikilinks_title_after_pipe',
                    format='vimwiki',
                    outputfile=str(dest_file)
                )

                import re
                with open(dest_file, 'r', encoding='utf-8') as f:
                    md_text = f.read()

                # Post-process to remove extensive whitespace after bullet points
                md_text = re.sub(r'^(\s*-)\s{2,}', r'\1  ', md_text, flags=re.MULTILINE)

                with open(dest_file, 'w', encoding='utf-8') as f:
                    f.write(md_text)
            elif args.convert_vimwiki:
                # Source is markdown, dest is vimwiki
                dest_file = dest_dir / (source_file.stem + '.wiki')
                pypandoc.convert_file(
                    str(source_file),
                    'vimwiki',
                    format='markdown',
                    outputfile=str(dest_file)
                )

            print(f"Successfully converted and copied to {dest_file}")
        except ImportError:
            print("Error: pypandoc is not installed or pandoc binary is missing.")
        except Exception as e:
            print(f"Error during pandoc conversion: {e}")
    else:
        dest_file = dest_dir / source_file.name
        try:
            shutil.copy2(source_file, dest_file)
            print(f"Successfully copied to {dest_file}")
        except Exception as e:
            print(f"Error during file copy: {e}")
