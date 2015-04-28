#!/usr/bin/env python3
"""
The header module provides useful commands for parsing a header of a file.

As a stand-alone program, header will print out a newline separated list of all header terms to improve command-line
readability.
"""

__author__ = 'Alex H Wagner'


class Header(object):
    """A dictionary of strings constituting the header"""

    def __init__(self, filename='', header='', delimiter='Auto'):
        if filename:
            with open(filename) as f:
                self.header = f.readline().strip()
            if delimiter == 'Auto':
                if filename.endswith('tsv'):
                    delimiter = "\t"
                elif filename.endswith('csv'):
                    delimiter = ","
        elif header:
            self.header = header.strip()
        else:
            self.header = ""

        if delimiter == 'Auto':
            comma_split = header.split(",")
            tab_split = header.split("\t")
            if len(comma_split) > len(tab_split):
                split = comma_split
            else:
                split = tab_split
        else:
            split = header.split(delimiter)

        self.header_column = {}
        self.delimiter = delimiter
        self._parse(self.header, self.delimiter)

    def _parse(self, header, delimiter):
        for i, key in enumerate(header.split(delimiter)):
            self.header_column[key] = i

    def __str__(self):
        return "\n".join(sorted(self.header_column.keys(), key=lambda x: self.header_column[x]))

if __name__ == "__main__":
    import sys

    if len(sys.argv[1:]) > 1:
        first = True
        for file in sys.argv[1:]:
            if not first:
                print()     # Blank line spacer
            else:
                first = False
            print("<== " + file + " ==>")
            print("-" * (8 + len(file)))
            print(Header(file))
    else:
        print(Header(sys.argv[1]))