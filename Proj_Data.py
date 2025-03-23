import os
import json
import shutil
from subprocess import PIPE, run
import sys

PROJ_DIR_PATTERN = "Project" # Pattern to identify project directories


def find_all_proj_dirs(source):
    pass


def main(source, target):
    cwd = os.getcwd()
    source_path = os.path.join(cwd, source) #Adds path to the source directory relative to the current working directory
    target_path = os.path.join(cwd, target)


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        raise Exception("You must pass two arguments: the path to the project and the path to the data folder.")
    
    source, target = args[1:]
    main(source, target)