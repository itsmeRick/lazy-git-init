#!/bin/sh

cd
source ~/.env
python create.py $1
mkdir ~/Documents/projects/$1
cd ~/Documents/projects/$1
git init
git remote add origin git@github.com:$user/$1.git
touch README.md
git add .
git commit -m "Initial commit"
git push origin master

