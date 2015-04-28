#!/usr/bin/env python3

"""
A module for transforming excel-style csv files to tsv.
"""

__author__ = 'Alex H Wagner'

import sys
import csv

encoding = 'ISO-8859-1'


def transform(filename):
    with open(filename, encoding=encoding) as file:
        for l in csv.reader(file):
            print("\t".join(l))

if __name__ == '__main__':
    transform(sys.argv[-1])