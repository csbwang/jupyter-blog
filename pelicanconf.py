#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'warmber'
SITENAME = "warmber's Blog"
SITEURL = 'https://csbwang.github.io'
GITHUB_URL = 'https://github.com/csbwang'

PATH = 'content'

# Regional Settings
TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = 'zh'
DATE_FORMATS = {'zh' : '%Y-%m-%d(%a)'}

MARKUP = ('md', 'ipynb')
# Plugins and extensions
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid',
                'toc(permalink=true)']
PLUGIN_PATH = './pelican-plugins/'
PLUGINS = ['ipynb.markup', 'sitemap', 'extract_toc', 'tipue_search',
           'neighbors', 'latex', 'related_posts',
           'multi_part']

# Appearance
TYPOGRIFY = True
THEME = 'elegant'
DEFAULT_PAGINATION = False

# sitemap config
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.5,
        "indexes": 0.5,
        "pages": 0.5,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly",
    }
}

# Defaults
DEFAULT_CATEGORY = 'Notes'
USE_FOLDER_AS_CATEGORY = False
ARTICLE_URL = u'{slug}'
PAGE_URL = u'{slug}'
PAGE_SAVE_AS = u'{slug}.html'

# Feeds
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Social
SOCIAL = (
        ('Github', 'https://github.com/csbwang'),
          )

# elegant theme
static_paths = ['theme/images', 'images']
direct_templates = (('index', 'tags', 'categories', 'archives', 'search', '404'))
tag_save_as = ''
aUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
USE_SHORTCUT_ICONS = True

# Elegant Labels
SOCIAL_PROFILE_LABEL = 'Stay in Touch'
RELATED_POSTS_LABEL = 'Keep Reading'
#  SHARE_POST_INTRO = 'Like this post? Share on:'
#  COMMENTS_INTRO = 'So what do you think? Did I miss something? Is any part unclear? Leave your comments below.'

# Mailchimp
EMAIL_SUBSCRIPTION_LABEL = 'Get Monthly Updates'
EMAIL_FIELD_PLACEHOLDER = 'Enter your email...'
SUBSCRIBE_BUTTON_TITLE = 'Send me Free updates'
MAILCHIMP_FORM_ACTION = 'empty'

# comment config
DISQUS_SITENAME="FelixWang"
