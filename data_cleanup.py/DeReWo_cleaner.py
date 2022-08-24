# -*-coding:utf-8 -*-
# Author: Eileen Kammel, 811770

import re


def clean(filepath):
    with open(filepath, "r", encoding="ISO-8859-1") as infile:
        with open("DeReWo_cleaned.txt", "w", encoding="utf-8") as outfile:
            while True:
                line = infile.readline()
                if not line:
                    break
                if line.startswith("#"):
                    continue
                line = re.sub(r"([a-zA-Z]+)(\s.*|\W.*)", r"\1", line)
                outfile.write(line)
