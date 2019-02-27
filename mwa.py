#!/usr/bin/env python3

import os
import sys
import subprocess

script_dir = os.path.dirname(__file__)
words_file = os.path.join(script_dir, "words.txt")
cwd = os.getcwd()

os.chdir(script_dir)
subprocess.call(["git","pull"])
os.chdir(cwd)

with open(words_file) as f:
    banned_words = set(word.lower().strip() for word in f.readlines())

if(len(sys.argv) != 2):
    print("ERROR: Requires 1 argument of filename to scan")
    sys.exit(1)

file_path = os.path.join(cwd,sys.argv[1])
if not os.path.exists(file_path):
    print("ERROR: File %s does not exists" % file_path)

word_found = 0

with open(file_path) as f:
    for i,line in enumerate(f):
        for word in banned_words:
            if(word in line.lower().strip()):
                word_found += 1
                print("Found \"%s\" on line %d"%(word,i))

sys.exit(word_found)
