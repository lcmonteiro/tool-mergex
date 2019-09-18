# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
# extern
# ---------------------------------------------------------
from git.cmd  import Git
from git.exc  import GitCommandError
from sys      import argv
from argparse import ArgumentParser
from tempfile import TemporaryFile
from shutil   import copyfileobj as copy
from filecmp  import cmp         as equal
# ---------------------------------------------------------
# internal
# ---------------------------------------------------------
# from .native  import format
from .native  import minimize
# -----------------------------------------------------------------------------
# merge
# -----------------------------------------------------------------------------
def merge(current, base, other, type):
    try:
        # origin
        origin_corrent = TemporaryFile()
        origin_other   = TemporaryFile()
        copy(open(current,'rb'), origin_corrent)
        copy(open(other  ,'rb'), origin_other)
        origin_corrent.seek(0)
        origin_other.seek(0)
        # minimize files
        minimize(current, base, other, type)
        # normalize files
        #format(current, type)
        #format(base   , type)
        #format(other  , type)
        # check diff between current and other 
        if equal(current, other):
            # restore current with origin/current
            copy(origin_corrent, open(current, 'wb'))
            return 0
        # git merge tool
        Git().merge_file('-L', 'mine', '-L', 'base', '-L', 'theirs', current, base, other)
        # recheck diff between current and other
        if equal(current, other):
            # restore current with origin/other
            copy(origin_other, open(current, 'wb'))
            return 0
    except GitCommandError as e:
        # print('error', e.status)
        return e.status
    except Exception as e:
        print('exception', e)
        return 255
    return 0
# -----------------------------------------------------------------------------
# main - merge
# -----------------------------------------------------------------------------
def main_merge():
    parser = ArgumentParser()
    parser.add_argument('current', type=str, default = '')
    parser.add_argument('base',    type=str, default = '')
    parser.add_argument('other',   type=str, default = '')
    parser.add_argument('--type',  type=str, default = '')
    args = parser.parse_args()
    return merge(args.current, args.base, args.other, args.type)
# -----------------------------------------------------------------------------
# main - format
# -----------------------------------------------------------------------------
def main_format():
    parser = ArgumentParser()
    parser.add_argument('file'  , type=str, default = '')
    parser.add_argument('--type', type=str, default = '')
    args = parser.parse_args()
    return format(args.file, args.type)
# -----------------------------------------------------------------------------
# end
# -----------------------------------------------------------------------------