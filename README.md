# Image Compression Script

A command line script that compresses image(s) as much as possible without losing quality or resolution. The script supports JPEG, PNG and WEBP image formats and is built using open-source modules.

## Requirements
- Python 3.x
- PIL (Pillow)

## Usage
`python compress_image.py -f [file or directory path] -q [quality]`
- `-f` or `--file`: path of the image file or directory containing the images.
- `-q` or `--quality`: quality of compression from 0 to 100 (default is 95).
- `-h`: show help 

## Example
`python compress_image.py -f image.jpg -q 85`
or
`python compress_image.py -f images_folder -q 75`

## Note
The script only works for jpeg, png and webp files and you can extend it to other image file formats as well.
