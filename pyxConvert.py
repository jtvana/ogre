#!/usr/bin/env python3

import argparse
import sys
import re

#Pyxelate deps
from skimage import io

try:
    from pyxelate import Pyx, Pal
except ImportError:
    print("Failed to import Pyxelate -- Are the dependencies properly setup?")

# this might depend heavily on how the service running this is hosted
STANDARD_OUTPUT_PATH="./"

# Pokemon Palettes.
# Naming scheme is "game version - color group".
# There are a handful of different palettes for each pokemon group
pokePals = {
    'ylw-brown': Pal.from_hex(["#f8f8f8", "#e89050", "#884828", "#181818"]),
    # Custom Pokemon palette taken from Brandon James Greer's Sprite Analysis video 
    #https://www.youtube.com/watch?v=gwF0L55kIgg 
    'bjg-green': Pal.from_hex(["#ffffff","#DDEDAB", "#53D926", "#002633"])
}

# All images will be 1:1 aspect ratio so lets setup some basic sprite sizes
res = [32, 64, 128, 512]

# cut image size to 1/14 of the original
downsample_by = 14

#choose 5 colors to use as the palette
palette = 4 


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("INFILE", type=str, help="Input image filename.")
    parser.add_argument(
        "resolution",
        type=int,
        help="Downscale resolution." + f' One of: {res}',
        default=64,
    )
    parser.add_argument(
        "PALETTE",
        type=str,
        help="Color Palette." + f"One of: {list(pokePals)}",
        default=0,
    )

    args = parser.parse_args()
    #do the thing
    image = io.imread(args.INFILE)

    OUTFILE = STANDARD_OUTPUT_PATH + "converted." + args.INFILE.split(".")[1]

    pyx = Pyx(width=args.resolution, height=args.resolution, palette=pokePals[args.PALETTE], dither="naive")
    pyx.fit(image)
    new_image = pyx.transform(image)
    io.imsave(OUTFILE, new_image)

"""
### Run some sample commands on test images
image = io.imread("aaaa04.png")
# Naive dither will properly handle transparency and usually works well in making things feel blockier
#pyx = Pyx(factor=downsample_by, palette=palette, dither="naive")

pyx = Pyx(width=64, height=64, palette=pokePals['bjg-green'], dither="naive")

#bird_down = Pyx(width=64, height=64, palette=, dither="atkinson").fit_transform(bird)

pyx.fit(image)
new_image = pyx.transform(image)
io.imsave("output.png", new_image)
"""
if __name__ == "__main__":
    main()
