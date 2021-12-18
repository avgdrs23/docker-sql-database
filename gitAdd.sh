#!/bin/sh

#create git  repo to this project and push it to gitHub website
repo=$(basename $PWD)
git init; git add .;  git commit -m "first commit"; git branch -m main; git remote add origin git@github.com:avgdrs23/"${repo}"
git push -u origin main
