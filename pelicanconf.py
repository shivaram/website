#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Eric Jonas'
SITENAME = u'pywren'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
PLUGIN_PATHS = ['/Users/jonas/projects/pywren/pelican-plugins']

PLUGINS = ['i18n_subsites', ]


THEME = "pelican-bootstrap3"
BOOTSTRAP_THEME = 'simplex' 

HIDE_SIDEBAR=True
DISPLAY_CATEGORIES_ON_MENU=False
MENUITEMS=[('blog', "/archives.html"),
           ('getting started', "foo"),
           ('documentation', "foo"),
           ("examples", "foo"), 
           ("blog", "foo"), 
           ("code", "foo")]
GITHUB_URL="http://github.com/pywren/pywren"

# PLUGINS = ['summary', 'i18n_subsites', 'liquid_tags.img', 'liquid_tags.video',
#                           'liquid_tags.youtube', 'render_math',
#              'liquid_tags.include_code', 
#              'liquid_tags.literal', 'tipue_search']
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}


# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
