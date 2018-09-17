#! /bin/bash

# Filename: pushm 2016-12-12
# Author: Huoty <sudohuoty@gmail.com>
# Script starts from here:

for repo in `git remote`; do
    echo "=============== Pushing to $repo ==============="
    git push $repo master
done
