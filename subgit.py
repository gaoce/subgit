#!/usr/bin/env python
import argparse
import subprocess as sp


def parse_args():
    description = "Download a sub folder in a github repository"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('link', help='Github link for svn')
    parser.add_argument('sub', help='Sub folder in the repository')
    parser.add_argument('--branch', default='master',
                        help='Branch in the repository')
    # TODO set new folder name
    return parser.parse_args()


def download(args):
    if args.branch == 'master':
        branch = 'trunk'
    else:
        branch = args.branch

    sub_path = '{}/{}/{}'.format(args.link, branch, args.sub)

    # TODO check svn availability
    try:
        sp.check_call(['svn', 'checkout', sub_path])
    except sp.CalledProcessError:
        print('Sorry the folder cannot be downloader')


def main():
    args = parse_args()
    download(args)

if __name__ == '__main__':
    main()
