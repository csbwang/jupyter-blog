#!/bin/sh
datetime=$(date +%Y-%m-%d\ %H:%M:%S)
filename=$(date +%Y%m%d_%H_%M_%S)
cd /Users/phenix/Documents/jupyter-blog/content/
echo "Title: \nDate: ${datetime}\nModified: \nCategory: \nTags: \nSlug: \nAuthors: \nSummary: \nStatus: draft">${filename}.md
