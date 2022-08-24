# -*-coding:utf-8 -*-
# Author: Eileen Kammel, 811770

import argparse
from controller.controller import InteractiveMatcher

parser = argparse.ArgumentParser()
parser.add_argument(
    "-f", type=str, help="Path to either a .txt file containing a wordlist or a .pkl file containing a pre set-up and pickeled BK-Tree")

args = parser.parse_args()

file = args.f

test = InteractiveMatcher()

test.get_data(file)
test.find_matches()
