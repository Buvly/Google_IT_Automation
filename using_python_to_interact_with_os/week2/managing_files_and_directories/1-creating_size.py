#!/usr/bin/python3

import os

def create_python_script(filename):
    comments = "# Start of a new Python program"
    with open(filename, "w+") as f:
        f.write(comments)
        f.read()
        filesize = os.path.getsize(filename)
    return filesize

print(create_python_script("buvly.py"))
