# nester.py modules provide print_lol() method
from __future__ import print_function
import sys


def print_lol(the_list, indent=False, level=0, fh=sys.stdout):  # provide default value
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level + 1, fh)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end='', file=fh)  # end=" python 3.x
            print(each_item, file=fh)
