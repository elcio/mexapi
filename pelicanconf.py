#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

#################################
#
# Basic Settings
#
#################################

# Webserver related
SITEURL = 'http://mexapi.local'
OUTPUT_PATH = '/srv/www/htdocs/mexapi/'
RELATIVE_URLS = False

# Site metadata
AUTHOR = u'Deny Dias'
SITENAME = u'MexApi'
SITE_TITLE = 'Deny Dias personal weblog'
SITESUBTITLE = u'This is not an API'
SITE_DESCRIPTION = 'Deny Dias personal weblog. Includes his blog, links to his social accounts and resume. This is not an API.'
COPYRIGHT = u'MexApi is licensed under <a href="http://creativecommons.org/publicdomain/zero/1.0/" target="_blank">CC0</a>.'
COPYRIGHT_NOLINK = u'MexApi is licensed under CC0.'

# Locale
LOCALE = 'C'
DEFAULT_LANG = u'en'
TIMEZONE = 'America/Sao_Paulo'
DEFAULT_DATE_FORMAT = ('%c BRT')

# Theme parameters
THEME = 'themes/mexapi'
TYPOGRIFY = True
DEFAULT_PAGINATION = 4
SUMMARY_MAX_LENGTH = 66
DEFAULT_ORPHANS = 2
REVERSE_ARCHIVE_ORDER = True
DISPLAY_PAGES_SIDEBAR = False
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
PDF_GENERATOR = False
MENUITEMS = (('Archives', SITEURL + '/archives.html'),
             ('About Me', 'http://about.me/denydias'),)

# Sidebar
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 10

# Force the same URL structure as blogger.com
FILENAME_METADATA = '(?P<slug>.*)'
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'

# Deactivate localization
ARTICLE_LANG_SAVE_AS = False
PAGE_LANG_SAVE_AS = False

# Deactivate author URLs
AUTHOR_SAVE_AS = False
AUTHORS_SAVE_AS = False

#################################
#
# Feeds Settings
#
#################################

#Feeds
FEED_DOMAIN = SITEURL
FEED_MAX_ITEMS = 10
FEED_RSS = False
FEED_ATOM = False
FEED_ALL_RSS = False
FEED_ALL_ATOM = False
TRANSLATION_FEED_RSS = False
TRANSLATION_FEED_ATOM = False
TAG_FEED_RSS = False
TAG_FEED_ATOM = False
CATEGORY_FEED_RSS = False
CATEGORY_FEED_ATOM = False

#################################
#
# Social Settings
#
#################################

# Social links
GITHUB_URL = 'https://github.com/denydias'
TWITTER_URL = 'https://twitter.com/denydias'
GOOGLEPLUS_URL = 'https://plus.google.com/104343775245895695882'

#################################
#
# Path Settings
#
#################################

# Output
#OUTPUT_PATH = '/srv/www/htdocs/mexapi/'

# Static files
STATIC_PATHS = ['images',]

# A list of files to copy from the source to the destination
# A list of extra files to copy from the source to the destination
FILES_TO_COPY = (
                 ('../README.rst', 'README.rst'),
                 ('extras/404.html', '404.html'),
                 ('extras/CNAME', 'CNAME'),
                 ('extras/favicon.ico', 'favicon.ico'),
                 ('extras/ga_optout.html', 'ga_optout.html'),
                 ('extras/robots.txt', 'robots.txt'),
                )

#################################
#
# Plugins Settings
#
#################################

PLUGIN_PATH = 'plugins'
PLUGINS = ['assets', 'better_figures_and_images', 'html_rst_directive', 'multi_part', 'pelican_vimeo', 'pelican_youtube', 'related_posts',]

# Disable to avoid slow CSS minifying process
ENABLE_ASSETS = False

# Setting for the better_figures_and_images plugin
RESPONSIVE_IMAGES = True

# Settings for related_posts
RELATED_POSTS_MAX = 4

#################################
#
# Custom Jinja Filters
#   see: http://jinja.pocoo.org/docs/templates/#filters
#
#################################
