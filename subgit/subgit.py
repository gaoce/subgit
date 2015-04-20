#!/usr/bin/env python
from __future__ import print_function

import re
import argparse
import subprocess as sp
import sys
import os.path


def parse_args():
    description = "Download a folder or file in a github repository"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('link', help='Github link for svn')
    parser.add_argument('path', help='File or folder to download')
    parser.add_argument('--branch', default='master',
                        help='Branch in the repository')
    parser.add_argument('--software', default='git', choices=['git', 'svn'],
                        help='Software to be used, '
                             'either git (download single file or folder) '
                             'or svn (folder only)')
    # TODO set new folder name
    return parser.parse_args()


def download_git(args):

    # TODO check git availability
    try:
        sp.check_call(['git', 'clone', '-n', '--depth', '1', args.link])
    except sp.CalledProcessError:
        print('Sorry the folder cannot be downloaded', file=sys.stderr)
        sys.exit(1)

    # Convert svn link to git link
    if not args.link.endswith('.git'):
        link = args.link + '.git'
    else:
        link = args.link

    # Get repository name and cd into it
    repo_name = re.search('(.*?)\.git', os.path.basename(link)).group(1)
    os.chdir(repo_name)

    # Check out the desired path
    try:
        sp.check_call(['git', 'checkout', args.branch, args.path])
    except sp.CalledProcessError:
        print('The path is not available in the repo', file=sys.stderr)
        sys.exit(1)

    # Get out of here the repository
    os.chdir('..')


def download_svn(args):
    if args.branch == 'master':
        branch = 'trunk'
    else:
        branch = args.branch

    # Convert SSH or HTTPS link to svn link
    link = args.link.rstrip('.git')
    if link.startswith('git'):
        link = link.replace(':', '/')
        link = link.replace('git@', 'https://')

    sub_path = '{}/{}/{}'.format(link, branch, args.path)

    # TODO check svn availability
    try:
        sp.check_call(['svn', 'checkout', sub_path])
    except sp.CalledProcessError:
        print('Sorry the folder cannot be downloader')


def main():
    args = parse_args()
    if args.software == 'git':
        download_git(args)
    elif args.software == 'svn':
        download_svn(args)
    else:
        sys.exit(1)

if __name__ == '__main__':
    main()
