from PIL import Image
import sys
import os
from pathlib import Path


def get_files(source):
    exts = ['.jpg', '.jpeg', '.png', '.gif']
    files = []

    try:
        raw_files = os.listdir(source)
    except:
        return files
    
    for file in raw_files:
        if any(file.lower().endswith(ext) for ext in exts):
            files.append(file)
    return files


def convert_to_webp(filepath, saveas):
    image = Image.open(filepath)
    image.convert('RGB')
    image.save(f'{saveas}.webp',
               'webp',
               lossless=False,
               method = 6,
               quality = 80)


def main(source):
    files = get_files(source)
    for file in files:
        filepath = os.path.join(source, file)
        noext = Path(filepath.lower()).stem
        saveas = os.path.join(source, noext)
        convert_to_webp(filepath, saveas)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        source = sys.argv[1]
    else:
        print('This script requires 1 argument')
        print('python webp_time.py /spath/to/images/')
    main(source)