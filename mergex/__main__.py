# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
# extern
# ---------------------------------------------------------
from git      import Repo
from git.exc  import GitCommandError
from sys      import argv
from argparse import ArgumentParser
from tempfile import NamedTemporaryFile
from shutil   import copyfileobj as copy
from hashlib  import md5
# ---------------------------------------------------------
# internal
# ---------------------------------------------------------
from .native  import format
# -----------------------------------------------------------------------------
# md5
# -----------------------------------------------------------------------------
def md5sum(path):
    with open(path, 'r', encoding='utf-8') as f:
        return md5(f.read()).hexdigest()
    return ''
# -----------------------------------------------------------------------------
# merge
# -----------------------------------------------------------------------------
def temp_file():
    temp = NamedTemporaryFile('+w')
    return temp
# -----------------------------------------------------------------------------
# merge
# -----------------------------------------------------------------------------
def merge(current, base, other):
    try:
        # backup file
        backup = temp_file()
        copy(open(current), backup)
        # normalize files
        format(current)
        format(base)
        format(other)
        # check diff between current and other 
        if md5sum(current) == md5sum(other):
            # git merge tool
            return Repo().git.merge_file(current, base, other)
        else:
            # restore the current
            copy(backup, open(current, 'w'))
            return 0
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