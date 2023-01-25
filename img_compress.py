#!/usr/bin/env python

import argparse
from PIL import Image
import os

def compress_image(file_path, save_as=None, quality=95):
    """
    Compress an image and save it to a new file
    :param file_path: path of the image file to compress
    :param save_as: path to save the compressed image
    :param quality: quality of compression from 0 to 100
    :return: None
    """
    image = Image.open(file_path)
    file_ext = file_path.split('.')[-1]
    save_ext = 'JPEG' if file_ext in ['jpg', 'jpeg'] else 'PNG' if file_ext == 'png' else 'WEBP' if file_ext == 'webp' else None
    if not save_ext:
        print(f"{file_path} is not a valid file format. Only jpeg, png and webp are supported.")
        return
    if save_as:
        save_as = save_as.split('.')[0] + '.' + save_ext
        image.save(save_as, save_ext, quality=quality)
    else:
        image.save(file_path, save_ext, quality=quality)

def compress_images_in_dir(dir_path, quality=95):
    """
    Compress all images in a directory
    :param dir_path: path of the directory containing the images
    :param quality: quality of compression from 0 to 100
    :return: None
    """
    for filename in os.listdir(dir_path):
        if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png') or filename.endswith('.webp'):
            file_path = os.path.join(dir_path, filename)
            compress_image(file_path, quality=quality)
        else:
            print(f"{filename} is not a valid file format. Only jpeg, png and webp are supported.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Compress image(s)')
    parser.add_argument('-f', '--file', help='file or directory path')
    parser.add_argument('-q', '--quality', help='quality of compression from 0 to 100', type=int, default=95)
    args = parser.parse_args()

    file_path = args.file
    quality = args.quality

    if os.path.isfile(file_path):
        compress_image(file_path, quality=quality)
    elif os.path.isdir(file_path):
        compress_images_in_dir(file_path, quality=quality)
    else:
        print(f'{file_path} is not a valid file or directory')
