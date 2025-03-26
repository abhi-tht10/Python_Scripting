import os
import json
import shutil
from subprocess import PIPE, run
import sys

PROJ_DIR_PATTERN = "project" # Pattern to identify project directories


def find_all_proj_paths(source):
    proj_paths = []

    for root, dirs, files in os.walk(source):
        for directory in dirs:
            if PROJ_DIR_PATTERN in directory.lower():
                path = os.path.join(source, directory)
                proj_paths.append(path)
        break #only need to look through directories one time

    return proj_paths

def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)



def main(source, target):
    cwd = os.getcwd()
    source_path = os.path.join(cwd, source) #Adds path to the source directory relative to the current working directory
    target_path = os.path.join(cwd, target)

    proj_paths = find_all_proj_paths(source_path)
    print(proj_paths)


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        raise Exception("You must pass two arguments: the path to the project and the path to the data folder.")
    
    source, target = args[1:]
    main(source, target)