from PIL import Image
from os.path import basename
from sys import exit
import argparse

alphabet = "rgb0fRGBI"

parser = argparse.ArgumentParser()
parser.add_argument('-f', "--file", help="path to file", required=True)
parser.add_argument('-m', "--mode", help="rules of editing channels (see README.md for more info), random if blank")
parser.add_argument("--hide", action='store_true', help="do not show output image")
parser.add_argument('-o', "--output", help="path to the output")
parser.add_argument("--fullrand", action='store_true', help="if mode is random, use all possible combinations for random mode")
args = parser.parse_args()

file = args.file
mode = args.mode
name = basename(file)
try:
	img = Image.open(file)
except FileNotFoundError:
	print(f"Error: file {file} not found, exiting...")
	exit(1)

if not args.output and args.hide:  # nothing selected
	print("You asked to hide image, but didn't choose output file!\nUse -o/--output option for this\nExiting...")
	exit(1)
if mode == 'I':
	mode = 'RGB'
if not mode:  # generate random rules
	import random
	if args.fullrand:
		mode = "".join((random.choice(alphabet[:8]) for i in range(3)))
	else:
		mode = ''.join(random.sample('rgbRGB', 3))
	print("Mode: "+mode)
rules = list(mode)
for i, e in enumerate(rules):  # convert to numeric values
	rules[i] = alphabet.index(e)

pixarr = img.load()

for x in range(img.size[0]):
	for y in range(img.size[1]):
		p = pixarr[x, y][:3]  # strip alpha value
		mods = p + (0, 255, 255 - p[0], 255 - p[1], 255 - p[2])  # map pixel values to alphabet
		pixarr[x, y] = tuple(mods[rules[i]] for i in range(3))

if args.output:
	img.save(args.output)
	print(f"Image saved to {args.output}")
if not args.hide:
	title = name + " - " + mode
	img.show(title=title)
