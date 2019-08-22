#!/bin/sh

cd output
git add .
git commit -m "Updated Blog"
git push -u origin master
cd ..
git add .
git commit -m "Updated Blog"
git push -u origin master

