#! /bin/bash

# Filename: runserver.sh 2016-12-04
# Author: Huoty <sudohuoty@gmail.com>
# Script starts from here:

source /home/huoty/.virtualenvs/blog/bin/activate
export PYTHONPATH="/home/huoty/luring/"
export PYTHONUNBUFFERED=1
exec python -m server -p 8000 -r /home/server/blog/
