import difflib
import logging
import os
import shutil
from enum import Enum, auto

from .paths import FILES

log = logging.getLogger(__name__)


class ExecuteResult(Enum):
    MISSING_FILE = auto()
    NEW_FILE = auto()
    THE_SAME = auto()
    UPDATED = auto()


def open_file(path):
    try:
        with open(path) as f:
            return f.readlines()
    except FileNotFoundError:
        return None


def copy_(from_path, to_path):
    try:
        shutil.copy(from_path, to_path)
    except FileNotFoundError:
        dirs = to_path.split("/")
        dirs_path = [dir_ for dir_ in dirs if dir_]
        dirs_path = "/".join(dirs[:-1])
        os.makedirs(dirs_path)
        shutil.copy(from_path, to_path)


# TODO use more sophisticated type than str, Path
def process(from_path: str, to_path: str) -> ExecuteResult:
    result = None

    from_file = open_file(from_path)
    to_file = open_file(to_path)

    if not from_file:
        return ExecuteResult.MISSING_FILE

    if not to_file:
        result = ExecuteResult.NEW_FILE
    else:
        diff = difflib.context_diff(from_file, to_file)
        if not list(diff):
            return ExecuteResult.THE_SAME

    copy_(from_path, to_path)
    return result if result else ExecuteResult.UPDATED


def log_coping_result(result, from_path, to_path):
    if result == ExecuteResult.MISSING_FILE:
        log.info("missing file")
    elif result == ExecuteResult.NEW_FILE:
        log.info("New file")
    elif result == ExecuteResult.THE_SAME:
        log.info("the same")
    elif result == ExecuteResult.UPDATED:
        log.info("updated")


def execute_copy():
    for from_path, to_path in FILES.items():
        result = process(from_path, to_path)
        log_coping_result(result, from_path, to_path)


def execute_paste():
    for to_path, from_path in FILES.items():
        result = process(from_path, to_path)
        log_coping_result(result, from_path, to_path)
