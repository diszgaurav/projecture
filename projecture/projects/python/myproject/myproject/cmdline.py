"""command line interface to myproject
"""
__author__ = 'myproject:author_name'
__email__ = 'myproject:author_email'

#----------------------------------------------------------------------
import sys
import argparse

from .myproject import hello_world

#----------------------------------------------------------------------
def main(cmdline_args=None):

    if not cmdline_args:
        cmdline_args = sys.argv[1:]

    parser = argparse.ArgumentParser('my project command line')

    parser.add_argument('-e',
                        '--extend_hello',
                        action='store_true',
                        help='extends hello world greeting')

    args = parser.parse_args()

    hello_world(args.extend_hello)
