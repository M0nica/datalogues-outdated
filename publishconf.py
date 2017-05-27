#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

#SITEURL = '//m0nica.github.io/datalogues/'
SITEURL = 'http://datalogues.com'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""

# import pelican-theme
# THEME = "../pelican-themes/Medius"
# THEME = "../pelican-themes/Flex"
THEME = "../pelican-themes/attila"

# THEME = "../pelican-themes/gum"
