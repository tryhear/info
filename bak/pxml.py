#!/usr/bin/python

import shutil
import sys
import os
import uuid

def process_file(fn):
    SEP_KEY = '''Key=""'''

    if not os.path.exists(fn):
        print("File not exist: " + fn)
        return
    content = ""
    with open(fn, 'r', encoding="utf-8") as f:
        content = f.read()
    arr = content.split(SEP_KEY)
    if len(arr) == 1:
        print("No need to Process.")
        return

    new_content = ""
    for index, item in enumerate(arr):
        new_content += item
        if index!= len(arr) - 1:
            new_content += 'KEY="{0}"'.format(str(uuid.uuid1()).upper())

    shutil.copy(fn, fn + '.bak')
    with open(fn, 'w', encoding="utf-8") as f:
        f.write(new_content)
        print("Update file Done.")


if __name__ =='__main__':

    process_file(sys.argv[1])
