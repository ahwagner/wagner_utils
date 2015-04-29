#!/usr/bin/env python3

"""
A module for checking the md5 of a received file against a pre-computed checksum.
"""

__author__ = 'Alex H Wagner'

import hashlib
import argparse
import os


def compare_digest(hash_file, hash_string):
    m = hashlib.md5()
    with open(hash_file, 'rb') as f:
        buf = f.read(1024)
        m.update(buf)
        while buf:
            buf = f.read(1024)
            m.update(buf)
        md = m.hexdigest()
        return md == hash_string
        # if md == hash_string:
        #     print('Digest matches.')
        # else:
        #     print("Computed Digest: {0} does not match \nProvided Digest: {1}".format(md, hash_string))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__, prog='md5-check')
    parser.add_argument('-l', '--list', action='store_true',
                        help='infile is instead a list of file names and their expected md5 checksums')
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
                if compare_digest(hash_file, hash_string):
                    print('Digests match')
                else:
                    print("Digests do not match")
    else:
        if args['string'] is None:
            parser.print_usage()
            raise AttributeError('Must supply a string to compare against file digest.')
        if compare_digest(args['infile'], args['string']):
            print('Digests match')
        else:
            print("Digests do not match")