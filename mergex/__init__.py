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
        # backup
        backup = TemporaryFile()
        copy(open(current,'rb'), backup)
        backup.seek(0)
        # normalize files
        format(current)
        format(base)
        format(other)
        # check diff between current and other 
        if equal(current, other):
            # restore the current
            copy(backup, open(current, 'wb'))
            return 0
        # git merge tool
        return Git().merge_file(current, base, other)
    except GitCommandError as e:
        return e.status
    #except Exception as e:
    #    print('exception', e)
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