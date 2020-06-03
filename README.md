
# chwap
Swap and change RGB channels on image. Also, you can invert them with this tool.
## Installation
This tool is designed to work with Python 3, so it have to be installed. Also, you need python3-pip to install requirements. First, clone this repository and `cd` to it: `git clone https://github.com/gangural/chwap; cd chwap`. Then install the requirements (run as superuser): `pip3 install -r requirements.txt`. That's all!
## Usage
To get list of options, use `-h` flag:

    usage: chwap.py [-h] -f FILE [-m MODE] [--hide] [-o OUTPUT]
    
    optional arguments:
      -h, --help            show this help message and exit
      -f FILE, --file FILE  path to file
      -m MODE, --mode MODE  rules of editing channels (see README for more info).
                            Random if blank.
      --hide                don't show output image
      -o OUTPUT, --output OUTPUT
                            path to the output

**How to choose `--mode`?** Read this set of rules:
- `r` - red channel from image, `g` is green, `b` is blue;
- `R` - red channel from image, but inverted, `G` is inverted green, `B` is inverted blue;
- `0` - fill a channel with 00 (full channel erase);
- `f` - fill channel with FF (full channel fill);
- `I` - invert all channels, an alias for `RGB`.

First symbol is responsible for red channel, second is green, third is blue.

**Examples of `--mode` option:**
`grb` - swipe red and green channels;
`rbG` - swipe blue and green channels, than invert green channel;
`fR0` - fill red channel, invert red and make it green, clear blue channel.

## Examples:
Let's use this image as example:

![A gouldian finch](https://i.imgur.com/fY6YEIj.jpg)

`python3 chwap.py -m rbG -f ~/Pictures/gouldian_finch.jpg -o result.jpg --hide`

Output image:

![Output image](https://i.imgur.com/S6NfuD1.png)

By the way, you can choose any file extension for output image, such as `.bmp`, `.gif`, `.png` and others. See [Pillow docs about supported image formats](https://pillow.readthedocs.io/en/5.1.x/handbook/image-file-formats.html#fully-supported-formats) for more information.
## How it works
Let's consider an example above, with `rbG` mode. This schema is a good explanation:
![explanation](https://i.imgur.com/TE9k5uU.png)

## Why
I created this simple tool for fun and experimenting. Sometimes result is really amazing 😃. See `gallery` folder to view best results.
