#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Colin McLear'
SITENAME = u'Colin McLear'
SITEURL = ''

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# The default date format expected
DEFAULT_DATE_FORMAT = '%d %m %Y'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Enable pages in the menu
# Set clean urls for pages as well
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True
#PAGE_URL = '{slug}'
#PAGE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
#PAGE_LANG_URL = '{slug}-{lang}.html'
#PAGE_LANG_SAVE_AS = '{slug}-{lang}.html'}

#Set menu items
#MENUITEMS = [('Home', '/pages/Home.md')]

# Theme
THEME = "/Users/Roambot/Dropbox/Webpage/content/themes/basic"

# Internal Links
STATIC_PATHS = ['images', 'pdfs']

# Turn on Typogrify
TYPOGRIFY = True

# A list of files to copy from the source to the destination
FILES_TO_COPY = ( ('images/favicon.ico', 'favicon.ico'),('CNAME',
'CNAME'), )
