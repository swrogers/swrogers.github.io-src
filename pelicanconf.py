#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Shane Rogers'
SITENAME = "Shane's Blog"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

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
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images']

PLUGIN_PATHS = ['pelican-plugins']

PLUGINS = [
    'i18n_subsites',
    'liquid_tags.img',
    'liquid_tags.youtube',
    'liquid_tags.include_code',
    'liquid_tags.giphy',
    'tag_cloud',
]

JINJA_ENVIRONMENT = {
        'extensions': ['jinja2.ext.i18n']
}


THEME = 'pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'darkly'

TYPOGRIFY = True

# PHOTOS plugin settings
PHOTO_LIBRARY = "~/Pictures"
PHOTO_GALLERY = (1024, 768, 80)
PHOTO_ARTICLE = (760, 506, 80)
PHOTO_THUMB = (192, 144, 60)
PHOTO_SQUARE_THUMB = False
PHOTO_RESIZE_JOBS = 1
PHOTO_WATERMARK = False
