#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Alkimist Lab'
SITENAME = 'Alkimist Lab'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'UTC'

DEFAULT_LANG = 'sl'

# I18n settings - hide translations from default category/tag pages
I18N_UNTRANSLATED_ARTICLES = 'hide'
I18N_UNTRANSLATED_PAGES = 'hide'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Pelican', 'https://getpelican.com/'),
    ('Python.org', 'https://www.python.org/'),
)

# Social widget
SOCIAL = (
    ('Instagram', 'https://www.instagram.com/alkimist_lab'),
)

DEFAULT_PAGINATION = 10

# Custom categories for events and shop
USE_FOLDER_AS_CATEGORY = True

# Menu configuration
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

# Custom menu with language switcher in top right
MENUITEMS = (
    ('Dogodki / Events', '/category/events.html'),
    ('Izdelki / Shop', '/category/shop.html'),
    ('O Nas / About', '/pages/about.html'),
)

# Show translations directly on articles
DEFAULT_METADATA = {
    'status': 'published',
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme
THEME = 'themes/cebong'

# Static paths
STATIC_PATHS = ['images', 'extra']

# Plugins
# PLUGIN_PATHS = ['plugins']
# PLUGINS = []
