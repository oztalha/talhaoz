#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://talhaoz.com'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

THEME = "pelican-themes/voidy-bootstrap"
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['assets']

TYPOGRIFY = True
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'

# Following items are often useful when publishing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'

DISQUS_SITENAME = "talhaoz"
GOOGLE_ANALYTICS = "UA-10670869-10"
GOOGLE_ANALYTICS_SITEID = "UA-10670869-10"
TWITTER_USERNAME = "tozCSS"

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
