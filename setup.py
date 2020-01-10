# -----------------------------------------------------------------------------
# imports
# -----------------------------------------------------------------------------
from setuptools import setup, find_packages
# -----------------------------------------------------------------------------
# helpers
# -----------------------------------------------------------------------------
with open("README.md", "r") as fh:
    long_description = fh.read()
# -----------------------------------------------------------------------------
# setup
# -----------------------------------------------------------------------------
setup(
    name='mergex',  
    version='0.5',
    author="Luis Monteiro",
    author_email="monteiro.lcm@gmail.com",
    description="MergeXML",
    long_description=long_description,
    url="",
    packages=[
        'mergex',
        'mergex.native'
    ],
    package_data={
        'mergex.native': ['MergeXml', 'MergeXml.exe']
    },
    install_requires=[
        'gitpython'
    ],
    entry_points={
      'console_scripts': [
          'mergex    = mergex:main_merge',
          'comparex  = mergex:main_compare',
          'formatx   = mergex:main_format',
          'minimizex = mergex:main_minimize'
      ]
    },
 )
 # ----------------------------------------------------------------------------
 # end
 # ----------------------------------------------------------------------------
