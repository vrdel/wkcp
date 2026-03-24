import os
import urllib.parse
from pathlib import Path

from wkcp.copywiki import extract_all_local_images

def DeleteWikiHandle(args):
    source_file = Path(args.file)
    if not source_file.exists():
        print(f"Error: Source file '{source_file}' does not exist.")
        return

    try:
        with open(source_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error: Could not read source file '{source_file}': {e}")
        return

    local_images = extract_all_local_images(content)
    source_dir = source_file.parent

    # Delete referenced local images
    for img_path_str in local_images:
        img_path = Path(urllib.parse.unquote(img_path_str))
        
        # We only delete if it exists relative to the source document or is absolute and exists
        actual_img_path = source_dir / img_path if not img_path.is_absolute() else img_path

        if actual_img_path.exists() and actual_img_path.is_file():
            try:
                actual_img_path.unlink()
                print(f"Referenced image deleted: {actual_img_path}")
            except Exception as e:
                print(f"Warning: Failed to delete image {actual_img_path}: {e}")
        else:
            print(f"Info: Referenced image '{actual_img_path}' not found, skipping.")

    # Delete the wiki file itself
    try:
        source_file.unlink()
        print(f"Wiki file deleted: {source_file}")
    except Exception as e:
        print(f"Error: Failed to delete file {source_file}: {e}")
