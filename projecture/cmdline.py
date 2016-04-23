"""command line interface to projecture
"""
__author__ = "Gaurav Verma"
__email__  = "diszgaurav@gmail.com"

#----------------------------------------------------------------------
from . import create_project
import argparse
import sys

#----------------------------------------------------------------------
def main(cmdline_args=None):

    if not cmdline_args:
        cmdline_args = sys.argv[1:]

    parser = argparse.ArgumentParser()

    parser.add_argument('project',
                        type = str,
                        help = 'project name with path')

    parser.add_argument('--author_name',
                        type = str,
                        default = 'author_name',
                        help = 'author name')

    parser.add_argument('--author_email',
                        type = str,
                        default = 'author_email',
                        help = 'author email')

    parser.add_argument('--about',
                        type = str,
                        default = 'short description of project',
                        help = 'short description of project')

    args = parser.parse_args(cmdline_args)

    create_project(args.project,
                   author_name = args.author_name,
                   author_email = args.author_email,
                   about = args.about)
