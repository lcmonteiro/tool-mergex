# -*- coding: utf-8 -*-
# https://github.com/lcmonteiro/space-shape/tree/master/Applications/MergeXML
# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
from subprocess import call
from os.path    import dirname
from os.path    import abspath
from platform   import system
from functools  import reduce
# -----------------------------------------------------------------------------
# program path 
# -----------------------------------------------------------------------------
def program():
    if system() == 'Windows':
        return abspath('%s/MergeXml.exe'%(dirname(__file__)))
    return abspath('%s/MergeXml'%(dirname(__file__)))
# -----------------------------------------------------------------------------
# format
# -----------------------------------------------------------------------------
def format(type, file):
    return call([program(), 
        '-m', 'normalize',
        '-l', 'ERROR',
        '-f', type,
        '-i', file,
    ])
# -----------------------------------------------------------------------------
# minimize
# -----------------------------------------------------------------------------
def minimize(type, *files):
    return call([program(), 
        '-m', 'minimize',
        '-l', 'ERROR',
        '-f', type,
    ] + reduce(lambda v, e: v + ['-i', e], files, []))
# -----------------------------------------------------------------------------
# end
# -----------------------------------------------------------------------------
