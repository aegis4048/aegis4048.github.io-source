#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'ERIC SOOBIN KIM'
AUTHOR_SHORTENED = 'Eric'
AUTHOR_SUBTITLE = 'PYTHONIC THINKER & SOLVER, PETROLEUM ENGINEER'
SITENAME = 'Pythonic Excursions'
SITESUBTITLE = u'Stories about Python and Data Science'
SITE_DESCRIPTION = 'Pythonic Excursions | Stories about Python and Data Science'
SITEURL = 'https://aegis4048.github.io'

# Regional Settings
TIMEZONE = 'America/Los_Angeles'
DATE_FORMATS = {'en': '%b %d, %Y'}
DEFAULT_LANG = u'en'

# Plugins and extensions
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {
            'css_class': 'highlight'
        },
        'markdown.extensions.extra': {},
        'markdown.extensions.toc': {
            'permalink': 'true'
        },
        'markdown.extensions.meta': {},
        'markdown.extensions.admonition': {},
    }
}

MARKUP = ['md']
PLUGIN_PATHS = ['plugins/']
PLUGINS = ['sitemap',
           'extract_toc',
           'neighbors',
           'render_math',
           'related_posts',
           'share_post',
           'series',
           'tipue_search',
           'summary',       # auto-summarizing articles
           'feed_summary',  # use summaries for RSS, not full articles
           'ipynb.liquid',  # for embedding notebooks
           'liquid_tags.img',  # embedding images
           'liquid_tags.video',  # embedding videos
           'liquid_tags.include_code',  # including code blocks
           'liquid_tags.literal',
           ]
IGNORE_FILES = ['.ipynb_checkpoints']
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'hourly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Appearance
THEME = 'themes/aegis-jupyter'
DEFAULT_PAGINATION = False

# Defaults
DEFAULT_CATEGORY = 'Miscellaneous'
USE_FOLDER_AS_CATEGORY = True
ARTICLE_URL = u'{slug}'
PAGE_URL = u'{slug}'
PAGE_SAVE_AS = u'{slug}.html'

# Feeds
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None

CLAIM_GOOGLE = "ZsWFnpirKDgtbmwb1YRymDnSfvnUrpzCbf6LD1F_4TY"
CLAIM_BING = "8FF1B025212A47B5B27CC47163A042F0"

STATIC_PATHS = ['figures', 'downloads', 'images',]
DIRECT_TEMPLATES = (('index', 'archives', 'search', '404', 'about'))
AUTHOR_SAVE_AS = ''
USE_SHORTCUT_ICONS = True

# Labels
RELATED_POSTS_LABEL = 'Related Posts'       # articles that share common tags
SHARE_POST_INTRO = 'Share This Post :'

# SMO
FEATURED_IMAGE = SITEURL + '/theme/img/logo_icon_background.png'

# for liquid tags
CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'
MISC_DIR = 'downloads/misc'

ENABLE_MATHJAX = True

# files are actually saved in /themes/aegis-jupyter/static/img/, but its copied to /output/theme/img/.
# just store any meta files in /themes/aegis-jupyter/static/, and you are good.
PROFILE_PHOTO_FOOTER = "theme/img/profile_photo_footer.jpg"
PROFILE_PHOTO_ABOUT = "theme/img/profile_photo_about.jpg"
INDEX_BANNER_IMAGE = "theme/img/index_banner_image.jpg"
LOGO_WITH_SUBTITLE = "theme/img/logo_with_subtitle.svg"  # logo created at "https://vectr.com/"

# actually located in 'content/downloads/misc/'. Files in 'content/downloads' will be copied into 'output/downloads' to
# auto-generate html href link.
RESUME_PDF_LINK = 'downloads/misc/Resume_Spring_2019.pdf'
RESUME_BUTTON_TEXT = 'Download CV'

GITHUB_LINK = 'https://github.com/aegis4048'
LINKEDIN_LINK = 'https://www.linkedin.com/in/eric-kim-34318811b/'

ABOUT_PAGE = 'about.html'
ARCHIVE_PAGE = 'archives.html'

# when developing offline, set it as False.
USE_CDN = False


############################ Social Media Shares ############################

# About Page
ABOUT_PAGE_TITLE = 'About Eric'
ABOUT_PAGE_DESCRIPTION = 'Pythonic Thinker & Solver, Petroleum Engineer'

# Archive Page
ARCHIVE_PAGE_TITLE = 'Archive'
ARCHIVE_PAGE_DESCRIPTION = 'Full Archives of Pythonic Excursions'

# landing(index) page description
INDEX_PAGE_TITLE = 'Pythonic Excursions'
INDEX_PAGE_DESCRIPTION = u'Stories About Python and Data Science | by Eric Kim'

### social media share debugger
# Twitter: https://cards-dev.twitter.com/validator
# Facebook: https://developers.facebook.com/tools/debug/


##############################################################################

FOOTER_TITLE = 'ABOUT ERIC'
TEXT_FOOTER = 'Senior undergraduate student at the Univeristy of Texas at Austin, Hildebrand Department of Petroleum ' \
              'Engineering, the #1 petroleum engineering school in the US. I am a self-taught Python developer with ' \
              'strong engineering & statistical background. I am good at creating clean, easy-to-read codes for data ' \
              'analysis. I enjoy assisting my fellow engineers by developing accessible and reproducible codes.'
EMAIL = 'aegis4048@gmail.com'
COPYRIGHT_NOTICE = 'Handcrafted by me @2018'

INCLUDE_PROGRESSBAR = True
PROGRESSBAR_COLOR = '#24292e'

# turn off typografy. otherwise the codes in Jupyter won't properly be highlighted

##################################################################################################################
# code snippet for processing variables for auto-generation of Tech Stacks
NUM_MAX_STAR = 5
TECH_STACKS = {'Python': 5,
               'PostgreSQL': 3,
               'Bootstrap': 4,
               'HTML': 5,
               'Spotfire': 2,
               'Django': 4,
               'TimescaleDB': 4,
               'jQuery': 4,
               'CSS': 4,
               'MATLAB': 2,
               'Linux': 3,
               'Server & Network': 3,}


def process_techstacks(tech_dict, num_max_star):
    num_stacks = len(tech_dict)
    tech_stacks_list = [{key: {'filled_star': value, 'empty_star': num_max_star - value }} for key, value in tech_dict.items()]
    tech_stacks_left = tech_stacks_list[:num_stacks // 2 + num_stacks % 2]
    tech_stacks_right = tech_stacks_list[num_stacks // 2 + num_stacks % 2:]
    return tech_stacks_left, tech_stacks_right


TECH_STACKS_LEFT, TECH_STACKS_RIGHT = process_techstacks(TECH_STACKS, NUM_MAX_STAR)

##################################################################################################################

PORT = 8090

# git submodule add https://github.com/aegis4048/aegis4048.github.io.git output
# git rm --cached output
# rm -rf .git/modules/output


DISQUS_SITENAME = "pythonic-excursions"
GOOGLE_ANALYTICS = "UA-133310548-1"