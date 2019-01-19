#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'ERIC SOOBIN KIM'
AUTHOR_SHORTENED = 'Eric'
AUTHOR_SUBTITLE = 'PYTHONIC THINKER & SOLVER, PETROLEUM ENGINEER'
SITENAME = 'Pythonic Excursions'
SITESUBTITLE = u'Stories about Python and Data Science'
SITEURL = '/'

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
           'assets',
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
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Appearance
THEME = 'themes/elegant'
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

# Social
SOCIAL = (('Github', 'https://github.com/Pelican-Elegant/'), ('RSS', SITEURL + '/feeds/all.atom.xml'))

CLAIM_GOOGLE = "Bk4Z5ucHLyPXqlZlj5LzANpYBBSvxqBW4E8i-Kwf-bQ"
CLAIM_BING = "8FF1B025212A47B5B27CC47163A042F0"

# Elegant theme
STATIC_PATHS = ['theme/images', 'figures', 'downloads','images', 'extra/robots.txt']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'}
}
DIRECT_TEMPLATES = (('index', 'archives', 'search', '404', 'about'))
AUTHOR_SAVE_AS = ''
USE_SHORTCUT_ICONS = True

# Elegant Labels
SOCIAL_PROFILE_LABEL = u'Stay in Touch'
RELATED_POSTS_LABEL = 'Related Posts'       # articles that share common tags
SHARE_POST_INTRO = 'Share This Post :'
COMMENTS_INTRO = u'So what do you think? Did I miss something? Is any part unclear? Leave your comments below.'

# Mailchimp
EMAIL_SUBSCRIPTION_LABEL = u'Get Monthly Updates'
EMAIL_FIELD_PLACEHOLDER = u'Enter your email...'
SUBSCRIBE_BUTTON_TITLE = u'Send me Free updates'
MAILCHIMP_FORM_ACTION = u'empty'

# SMO
TWITTER_USERNAME = u''
FEATURED_IMAGE = SITEURL + '/theme/images/apple-touch-icon-152x152.png'

# Legal
SITE_LICENSE = """Elegant theme documentation is licensed under a <a rel="license" 
    href="http://creativecommons.org/licenses/by/4.0/">
    Creative Commons Attribution 4.0 International License</a>.""" 

# SEO
SITE_DESCRIPTION = u'Documentation website for Pelican-Elegant theme originally created by Talha Mansoor'

# Landing Page
PROJECTS = [
    {
        'name': 'Elegant', 
        'url': 'https://github.com/Pelican-Elegant/elegant',
        'description': 'A clean and distraction free Pelican theme, with search and a lot more unique features. Built '
            'with Jinja2 and Bootstrap'
    },
    {
        'name': 'Elegant Documentation', 'url': 'https://github.com/Pelican-Elegant/documentation',
        'description': 'Documentation repository for Pelican-Elegant theme'
    }
]

LANDING_PAGE_ABOUT = {
    'title': 'Live demonstration and documentation of Pelican-Elegant Theme',
    'details': """<p>This page serves both as documentation site and demonstration of Pelican-Elegant theme 
        capabilities and look&amp;feel.</p><p>Please do check our Project pages and browse this site for more information.
        </p>"""
}

# for liquid tags
CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'
MISC_DIR = 'downloads/misc'


ENABLE_MATHJAX = True

# files are actually saved in /themes/elegant/static/img/, but its copied to /output/theme/img/.
# just store any meta files in /themes/elegant/static/, and you are good.
# logo created at "https://vectr.com/"
LOGO_WITH_SUBTITLE = "theme/img/logo_with_subtitle.svg"
PROFILE_PHOTO_FOOTER = "theme/img/profile_photo_footer.jpg"
PROFILE_PHOTO_ABOUT = "theme/img/profile_photo_about.jpg"
INDEX_BANNER_IMAGE = "theme/img/index_banner_image.jpg"

# actually located in 'content/downloads/misc/'. Files in 'content/downloads' will be copied into 'output/downloads' to
# auto-generate html href link.
RESUME_PDF_LINK = 'downloads/misc/Resume_Spring_2019.pdf'
RESUME_BUTTON_TEXT = 'Download CV'

GITHUB_LINK = 'https://github.com/aegis4048'
LINKEDIN_LINK = 'https://www.linkedin.com/in/eric-kim-34318811b/'

ABOUT_PAGE = 'about.html'
ARCHIVE_PAGE = 'archives.html'

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
