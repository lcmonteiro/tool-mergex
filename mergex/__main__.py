# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
from git      import Repo
from git.exc  import GitCommandError
from sys      import argv
from argparse import ArgumentParser
from tempfile import NamedTemporaryFile
from shutil   import copy2 as copy
from .native  import format
# -----------------------------------------------------------------------------
# merge
# -----------------------------------------------------------------------------
def temp_file():
    temp = NamedTemporaryFile()
    return temp
# -----------------------------------------------------------------------------
# merge
# -----------------------------------------------------------------------------
def merge(current, base, other):
    try:
        #temp = temp_file()
        #copy(current, temp.name)
        #copy(temp.name, current)

        format(current)
        format(base)
        format(other)
        return Repo().git.merge_file(current, base, other)
    except GitCommandError as e:
        return e.status
    except Exception as e:
        print(e)
        pass
    return 255
# -----------------------------------------------------------------------------
# main
# -----------------------------------------------------------------------------
def main():
    parser = ArgumentParser()
    parser.add_argument('current', type=str, default = '')
    parser.add_argument('base',    type=str, default = '')
    parser.add_argument('other',   type=str, default = '')
    args = parser.parse_args()
    return merge(args.current, args.base, args.other)
# -----------------------------------------------------------------------------
# end
# -----------------------------------------------------------------------------