#!/usr/bin/env python3
# ----------------------------------------------------------------------------
# Purpose : Demonstrating common file handling shell commands
# Author:       Denny Vettom
# Dependencies: PYTHON 3
#

import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile


def main():
    print (" ------- This is Main Function ")

    # Make a duplicate of file
    if path.exists("testfile.txt"):
        SRC = path.realpath("testfile.txt")

        # Make backup copy by addign .bak
        DST = SRC + ".bak"

        # Copy over the permissions, mod times and other info
        shutil.copy(SRC, DST)
        shutil.copystat(SRC, DST)

        # Rename original file
        os.rename("testfile.txt", "newfile.txt")

        # Put things in to Zip archive.

         # Now put things to archive
        root_dir, tail = path.split(SRC)
        shutil.make_archive("archive", "zip", root_dir)

        # Backup specific file
        with ZipFile("testzip.zip" , "w") as newzip:
            newzip.write("testfile.txt")
            newzip.write("calendar.py")




if __name__ == "__main__":
    main ()