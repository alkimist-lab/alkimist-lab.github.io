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

# Blogroll (disabled for Flex)
# LINKS = ()

DEFAULT_PAGINATION = 10

# Custom categories for events and items
USE_FOLDER_AS_CATEGORY = True

# Menu configuration
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True
MAIN_MENU = True

# Show translations directly on articles
DEFAULT_METADATA = {
    'status': 'published',
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme
THEME = 'themes/Flex'

# Flex theme configuration
SITETITLE = 'Alkimist Lab'
SITESUBTITLE = 'Kovačke delavnice / Blacksmithing workshops'
SITEDESCRIPTION = 'Alkimist Lab - Rokodelske delavnice v Sloveniji'

# Flex theme - Dark mode
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

# Flex theme - Main menu items
MENUITEMS = (
    ('Dogodki', '/category/events.html'),
    ('Izdelki', '/category/items.html'),
    ('English', '/en/index.html'),
)

# Flex theme - Social media
SOCIAL = (
    ('instagram', 'https://www.instagram.com/alkimist_lab'),
)

# Flex theme - Copyright
COPYRIGHT_YEAR = 2026
COPYRIGHT_NAME = 'Alkimist Lab'

# Static paths
STATIC_PATHS = ['images', 'extra']

# Plugins
PLUGINS = ['pelican.plugins.i18n_subsites']

# i18n_subsites configuration
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

I18N_SUBSITES = {
    'en': {
        'SITENAME': 'Alkimist Lab',
        'SITESUBTITLE': 'Blacksmithing workshops and more',
        'MENUITEMS': (
            ('Events', '/category/events.html'),
            ('Items', '/category/items.html'),
            ('English', '/en/index.html'),
            ('Slovensko', '/index.html'),
        )
    }
}
