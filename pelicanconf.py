#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'ERIC SOOBIN KIM'
AUTHOR_SUBTITLE = 'PYTHONIC THINKER & SOLVER, PETROLEUM ENGINEER'
SITENAME = 'Pythonic Excursions'
SITESUBTITLE = u'Stories about Python and Data Science'
SITEURL = ''
PATH = 'content'
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Set the article URL
ARTICLE_URL = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#MARKUP = ('md', 'ipynb')
#PLUGINS = ['ipynb.markup']

MARKUP = ['md']
PLUGIN_PATHS = ['./plugins', './plugins/pelican-plugins']
PLUGINS = [
    'summary',       # auto-summarizing articles
    'feed_summary',  # use summaries for RSS, not full articles
    'ipynb.liquid',  # for embedding notebooks
    'liquid_tags.img',  # embedding images
    'liquid_tags.video',  # embedding videos
    'liquid_tags.include_code',  # including code blocks
    'liquid_tags.literal',
    'tipue_search.tipue_search',
]
IGNORE_FILES = ['.ipynb_checkpoints']

# for liquid tags
CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'
MISC_DIR = 'downloads/misc'

# THEME SETTINGS
THEME = './theme/'

SHOW_ARCHIVES = True
SHOW_FEED = False  # Need to address large feeds

ENABLE_MATHJAX = True

STATIC_PATHS = ['images', 'figures', 'videos', 'downloads', 'favicon.ico', 'logo_with_subtitle.svg', 'logo_no_subtitle.svg', 'logo_icon.svg']

ABOUT_PAGE = '/pages/about.html'

# logo created at https://vectr.com/
LOGO_WITH_SUBTITLE = '/logo_with_subtitle.svg'
LOGO_ICON = '/logo_icon.svg'

# Footer info
LICENSE_URL = ""
LICENSE = ""

READERS = {'html': None}

GITHUB_LINK = 'https://github.com/aegis4048'
LINKEDIN_LINK = 'https://www.linkedin.com/in/eric-kim-34318811b/'
PROFILE_INTRODUCTION = 'My name is Eric Kim - Web Developer, Data Scientist, and Petroleum Engineer. \n SOMETHING'

import os

if not os.path.exists('output'):
    os.makedirs('output')


