#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

#################################
#
# Basic Settings
#
#################################

SITEURL = 'http://mexapi.macpress.com.br'
RELATIVE_URLS = False
DELETE_OUTPUT_DIRECTORY = True

#################################
#
# Feeds Settings
#
#################################

FEED_DOMAIN = SITEURL
FEED_RSS = 'feeds/rss.xml'
FEED_ATOM = 'feeds/atom.xml'

#################################
#
# Plugins Settings
#
#################################

PLUGINS = PLUGINS + ['gzip_cache', 'optimize_images', 'sitemap']

# Enable/disable assets for quick dev
ENABLE_ASSETS = True

# Settings for sitemap
SITEMAP = {
  'format': 'xml',
  'priorities': {
    'articles': 0.8,
    'indexes': 0.7,
    'pages': 0.5
    },
  'changefreqs': {
    'articles': 'weekly',
    'indexes': 'daily',
    'pages': 'monthly'
    }
  }

#################################
#
# External Services Settings
#
#################################

DISQUS_SITENAME = 'mexapi'
GOOGLE_ANALYTICS_ID = 'UA-43437542-1'
GOOGLE_ANALYTICS_SITENAME = 'MexApi'