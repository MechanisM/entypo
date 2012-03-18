#!/usr/bin/env python

import argparse
import yaml
import fontforge

KERNING = 15
SFD_TEMPLATE = '../src/font_template.sfd'

parser = argparse.ArgumentParser(description='Font builder tool')
parser.add_argument('-c', '--config', type=str, help='Config example: ../config.yml', required=True)
parser.add_argument('-i', '--svg_dir', type=str, help='Input svg file', required=True)
parser.add_argument('-o', '--ttf_file', type=str, help='Output ttf file', required=True)

args = parser.parse_args()

config = yaml.load(open(args.config, 'r'))

font = fontforge.open(SFD_TEMPLATE)

for name, glyph in config['glyphs'].iteritems():
    c = font.createChar(int(glyph['code']))

    c.importOutlines(args.svg_dir + '/' + name + '.svg')
    c.left_side_bearing = KERNING
    c.right_side_bearing = KERNING

font.generate(args.ttf_file)