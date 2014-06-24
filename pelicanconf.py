#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Colin McLear'
SITENAME = u'Colin McLear'
SITEURL = ''

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'
GOOGLE_ANALYTICS = 'UA-30497236-1'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = 10
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
#CLEAN_URLS = True


THEME = "content/themes/two-column"
#THEME = "/Users/Roambot/Dropbox/Webpage/content/themes/basic"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Internal Links
STATIC_PATHS = ['images', 'pdfs', 'pages', 'themes', 'extras/CNAME']
EXTRA_PATH_METADATA = {'extras/CNAME': {'path': 'CNAME'},}

# Turn on Typogrify
TYPOGRIFY = True

# A list of files to copy from the source to the destination
#FILES_TO_COPY = ( ('images/favicon.ico', 'favicon.ico'),('CNAME', 'CNAME'), )

USER_LOGO_URL = 'themes/two-column/static/images/me.jpg'
