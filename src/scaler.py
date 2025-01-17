from argparse import ArgumentParser
from math import floor
from PIL import Image
import os


def downscale_by_ratio(img, ratio, method=Image.BICUBIC, magic_crop=False):
    if ratio == 1: return img

    w, h = img.size
    if magic_crop:
        img = img.crop((0, 0, w - w % ratio, h - h % ratio))
        w, h = img.size

    w, h = floor(w / ratio), floor(h / ratio)
    return img.resize((w, h), method)


def parse_args():
    parser = ArgumentParser(description='Downscale')
    parser.add_argument('-i', '--input', help='Input dir')
    parser.add_argument('-o', '--output', help='Output dir')

    parser.add_argument(
        '-r',
        '--ratio',
        help='scale ratio e.g. 2, 4 or 8',
        type=int,
        required=True)

    args = parser.parse_args()

    return args


if __name__ == '__main__':
    # Parse command-line arguments
    args = parse_args()
    os.mkdir(args.output)
    for file in os.listdir(args.input):
     filename = os.fsdecode(file)
     if filename.endswith(".png") : 
        img = Image.open(args.input+"/"+filename)
        img_scaled = downscale_by_ratio(img, args.ratio)

        img_scaled.save(args.output+"/"+filename)
     else:
         continue
    