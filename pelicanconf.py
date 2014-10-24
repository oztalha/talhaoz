#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Talha Oz'
SITENAME = u'Breadcrumbs'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

SITESUBTITLE ='Sub-title that goes underneath site name in jumbotron.'
SITETAG = "Text that's displayed in the title on the home page."

# Extra stylesheets, for bootstrap overrides or additional styling.
STYLESHEETS = ("pygment.css", "voidybootstrap.css",)

# Use the default sharing button implementation.
CUSTOM_ARTICLE_SHARING = "sharing.html"
CUSTOM_ARTICLE_SCRIPTS = "sharing_scripts.html"

SOCIAL = (('Twitter', 'https://twitter.com/tozCSS',
         'fa fa-twitter-square fa-fw fa-lg'),
        ('LinkedIn', 'http://linkedin.com/in/oztalha',
         'fa fa-linkedin-square fa-fw fa-lg'),
        ('GitHub', 'http://github.com/oztalha',
         'fa fa-github-square fa-fw fa-lg'),
        )
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
