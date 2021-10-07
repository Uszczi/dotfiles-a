import os
import shutil

from .paths import FILES


# TODO use more sophisticated type than str, Path
def process(from_path: str, to_path: str):
    try:
        shutil.copy(from_path, to_path)
    except FileNotFoundError:
        dirs = to_path.split("/")
        dirs_path = [dir_ for dir_ in dirs if dir_]
        dirs_path = "/".join(dirs[:-1])
        os.makedirs(dirs_path)
        shutil.copy(from_path, to_path)


def execute_copy():
    for from_path, to_path in FILES.items():
        process(from_path, to_path)


def execute_paste():
    for to_path, from_path in FILES.items():
        process(from_path, to_path)