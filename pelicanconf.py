#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Spencer Chan'
SITENAME = 'Spencer Chan'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'US/Central'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

GITHUB_URL = 'http://github.com/spencerchan'
# Blogroll
'''LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)'''

# Social widget
SOCIAL = (('github', GITHUB_URL),)
DEFAULT_PAGINATION = 10

TAGLINE = "aspiring data scientist / pythonista / malört caucus"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

IPYNB_SKIP_CSS=True
THEME = 'themes/pelican-hss'

STATIC_PATHS = ['extra']
CUSTOM_CSS = '/static/custom.css'
EXTRA_PATH_METADATA = {
	'extra/custom.css': {'path': 'static/custom.css'},
}