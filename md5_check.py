#!/usr/bin/env python3

"""
A module for checking the md5 of a received file against a pre-computed checksum.
"""

__author__ = 'Alex H Wagner'

import hashlib
import argparse


def compare_digest(hash_file, hash_string):
    m = hashlib.md5
    with open(hash_file, 'b') as f:
        m.update(f)
        md = m.hexdigest()
        if md == hash_string:
            print('Digest matches.')
        else:
            print('Digest %s does not match %s.'.format(md, hash_string))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__, prog='md5-check')
    parser.add_argument('-l', '--list', action='store_true',
                        help='infile is a list of file names and their expected md5 checksums')
    parser.add_argument('infile')
    parser.add_argument('string', nargs='?',
                        help='a string to compare against the file digest (mutually exclusive with -l)')
    args = vars(parser.parse_args())

    if args['list']:
        if args['string']:
            parser.print_usage()
            raise AttributeError('String for file digest should not be supplied when using -l')
        with open(args['infile']) as file_list:
            for line in file_list:
                hash_file, hash_string = line.split("\t")
                print(hash_file + ': ', end="")
                compare_digest(hash_file, hash_string)
    else:
        if args['string'] is None:
            parser.print_usage()
            raise AttributeError('Must supply a string to compare against file digest.')

    if args['list'] and args['string']:
        compare_digest(args['infile'], args['string'])