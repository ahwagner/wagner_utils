#!/usr/bin/env python3

"""
A module for checking the md5 of a received file against a pre-computed checksum.
"""

__author__ = 'Alex H Wagner'

import hashlib
import argparse


def compare_digest(hash_file, hash_string):
    m = hashlib.md5()
    with open(hash_file, 'rb') as f:
        buf = f.read(1024)
        m.update(buf)
        while buf:
            buf = f.read(1024)
            m.update(buf)
        md = m.hexdigest()
        if md != hash_string:
            return md
        else:
            return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__, prog='md5-check')
    parser.add_argument('-l', '--list', action='store_true',
                        help='infile is instead a tab-delimited list of file names and their expected md5 checksums')
    parser.add_argument('infile', help='infile is used to digest ')
    parser.add_argument('string', nargs='?',
                        help='a string to compare against the file digest '
                             '(omit when using --list flag)')
    args = vars(parser.parse_args())

    if args['list']:
        if args['string']:
            parser.print_usage()
            raise AttributeError('String for file digest should not be supplied when using -l')
        with open(args['infile']) as file_list:
            for line in file_list:
                hash_file, hash_string = line.split("\t")
                print('---{0}---'.format(hash_file))
                result = compare_digest(hash_file, hash_string.strip())
                if result is True:
                    print('Digests match')
                else:
                    print("Computed digest {0} does not match \n"
                          "provided digest {1}".format(result, hash_string.strip()))
    else:
        if args['string'] is None:
            parser.print_usage()
            raise AttributeError('Must supply a string to compare against file digest.')
            result = compare_digest(hash_file, hash_string)
            if result is True:
                print('Digests match')
            else:
                print("Computed digest {0} does not match \n"
                      "provided digest {1}".format(result, hash_string))