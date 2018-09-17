#! /bin/bash

# Filename: githook-post-receive.sh 2016-12-04
# Author: Huoty <sudohuoty@gmail.com>
# Script starts from here:

PRO_IDR=/home/huoty/luring

# Update code
git --work-tree=$PRO_IDR --git-dir=$PRO_IDR/.git checkout -f HEAD

# Build site
jekyll build -s $PRO_IDR -d /home/server/blog

# clint config:
#   git remote add vultr ssh://huoty@vultrhost:/home/huoty/luring
#
# server .git/config add:
#   [receive]
#       denyCurrentBranch = ignore
#
# install hook:
#   cd .git/hooks/
#   ln -s ../../tools/githook-post-receive.sh post-receive
