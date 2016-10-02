#! /bin/bash

sudo git add .
echo "Set a comment for commit:"
read commitComment 
sudo git commit evolution.py -m "$commitComment"
sudo git push https://github.com/ConTcoN/Evolution
