import base64
import re
from pathlib import Path

from wkcp.utils import build_image_filename

def ExtractEmbeddedHandle(args):
    file_path = Path(args.file)
    if not file_path.exists() or not file_path.is_file():
        print(f"Error: {file_path} does not exist.")
        return
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Matches: ![<alt_text>](data:image/<ext>;base64,<payload>)
    pattern = re.compile(r'!\[(.*?)\]\(data:image/([a-zA-Z0-9]+);base64,([a-zA-Z0-9+/=]+)\)')
    
    def replacer(match):
        alt_text = match.group(1)
        ext = match.group(2)
        b64data = match.group(3)
        img_data = base64.b64decode(b64data)
        
        # We need a dummy path to pass to build_image_filename so it can extract the extension
        dummy_path = f"dummy.{ext}"
        new_filename = build_image_filename(dummy_path, microsec=True)
        
        new_file_path = file_path.parent / new_filename
        
        with open(new_file_path, 'wb') as f:
            f.write(img_data)
        
        print(f"Extracted base64 image to {new_file_path}")
        
        # Ensure we just output the filename if the output is in the same directory
        return f"![{alt_text}]({new_filename})"

    new_content, count = pattern.subn(replacer, content)
    
    if count > 0:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file_path} with {count} extracted image(s).")
    else:
        print("No base64 images found.")
