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
from .native  import format
# -----------------------------------------------------------------------------
# merge
# -----------------------------------------------------------------------------
def merge(current, base, other):
    try:
        # origin
        origin_corrent = TemporaryFile()
        origin_other   = TemporaryFile()
        copy(open(current,'rb'), origin_corrent)
        copy(open(other  ,'rb'), origin_other)
        origin_corrent.seek(0)
        origin_other.seek(0)
        # normalize files
        format(current)
        format(base)
        format(other)
        # check diff between current and other 
        if equal(current, other):
            # restore current with origin/current
            copy(origin_corrent, open(current, 'wb'))
            return 0
        # git merge tool
        Git().merge_file(current, base, other)
        # recheck diff between current and other
        if equal(current, other):
            # restore current with origin/other
            copy(origin_other, open(current, 'wb'))
            return 0
    except GitCommandError as e:
        print('error', e.status)
        return e.status
    except Exception as e:
        print('exception', e)
        return 255
    return 0
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