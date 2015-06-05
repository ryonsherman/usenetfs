#!/usr/bin/env python2

__author__    = "Ryon Sherman"
__email__     = "ryon.sherman@gmail.com"
__copyright__ = "Copyright 2015, Ryon Sherman"
__license__   = "MIT"

import fuse


class Usenet(fuse.Operations, fuse.LoggingMixIn):
    def __init__(self, index):
        print index

def main():
    import argparse

    parser = argparse.ArgumentParser(prog='usenetfs')
    parser.add_argument('index', metavar='index.nzb')
    parser.add_argument('mountpoint')

    args = parser.parse_args()
    print args

    try:
        fs = fuse.FUSE(Usenet(args.index), args.mountpoint)
    except:
        pass

if __name__ == '__main__':
    main()