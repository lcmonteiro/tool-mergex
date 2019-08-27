# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
from git      import Repo
from sys      import argv
from argparse import ArgumentParser
from .native  import format
# -----------------------------------------------------------------------------
# merge
# -----------------------------------------------------------------------------
def merge(current, base, other):
    try:
        format(current)
        format(base)
        format(other)
        return Repo().git.merge_file(current, base, other)
    except Exception as e:
        print(e)
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