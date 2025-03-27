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

def change_names_from_paths(paths, to_add):
    new_names = []
    for path in paths:
        _, dir_name = os.path.split(path)
        new_dir_name = dir_name.replace(to_add, "Compiled_Project")
        new_names.append(new_dir_name)

    return new_names

def copy_and_overwrite(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    shutil.copytree(source,destination)

def main(source, target):
    cwd = os.getcwd()
    source_path = os.path.join(cwd, source) #Adds path to the source directory relative to the current working directory
    target_path = os.path.join(cwd, target)
    
    create_dir(target_path)
    
    proj_paths = find_all_proj_paths(source_path)
    new_proj_paths = change_names_from_paths(proj_paths, "Project")

    for src, dest in zip(proj_paths, new_proj_paths):
        dest_path = os.path.join(target_path, dest)
        copy_and_overwrite(src, dest_path)


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        raise Exception("You must pass two arguments: the path to the project and the path to the data folder.")
    
    source, target = args[1:]
    main(source, target)