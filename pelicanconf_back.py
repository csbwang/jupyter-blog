#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'FelixWang'
SITENAME = "FelixWang's Blog"
SITEURL = 'https://csbwang.github.io'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'zh'
DATE_FORMATS = {'zh' : '%Y-%m-%d(%a)'}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
#  SOCIAL = (('You can add links in your config file', '#'),
#            ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['ipynb.markup', 'sitemap']
THEME = 'elegant'

# sitemap config
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.7,
        "indexes": 0.5,
        "pages": 0.3,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly",
    }
}

# elegant config
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

# blog relative file config
STATIC_PATHS=["imgs","extra"]
EXTRA_PATH_METADATA = {
    # 'extra/CNAME': { 'path': 'CNAME' }, # DNS config
    'extra/favicon.ico': { 'path': 'favicon.ico' },
    # 'extra/robots.txt': { 'path': 'robots.txt' },
}

# comment config
DISQUS_SITENAME="FelixWang"
