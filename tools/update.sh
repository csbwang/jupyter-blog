#!/bin/sh
commitstr=$(date +%Y%m%d_%H_%M_%S)
cd /Users/phenix/Documents/jupyter-blog/
make html
cd /Users/phenix/Documents/jupyter-blog/output/ 
git add .
git commit -m ${commitstr}
git push origin master
