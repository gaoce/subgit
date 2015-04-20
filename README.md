# subgit
Download a sub folder or file from a repository on github.com

## Install
In command line,
```
$ python setup.py install
```

## Usage

```
$ subgit -h
usage: subgit [-h] [--branch BRANCH] [--software {git,svn}] link path

Download a folder or file in a github repository

positional arguments:
  link                  Github link for svn
  path                  File or folder to download

optional arguments:
  -h, --help            show this help message and exit
  --branch BRANCH       Branch in the repository
  --software {git,svn}  Software to be used, either git (download single file
                        or folder) or svn (folder only)
```

## Reference
Based on [this](http://stackoverflow.com/questions/7106012/download-a-single-folder-or-directory-from-a-github-repo) and [this](http://stackoverflow.com/questions/2466735/how-to-checkout-only-one-file-from-git-repository/2466755#2466755) question.

