#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Monica Powell'
SITENAME = 'Datalogues'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TAG_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

SOCIAL = (
        ('Twitter', 'http://twitter.com/waterproofheart'),
        ('Email', 'mailto:monica@aboutmonica.com'),
        ('GitHub', 'https://github.com/M0nica'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# render ipynb as markdown
MARKUP = ('md', 'ipynb')

PLUGIN_PATH = './plugins'
PLUGINS = ['ipynb.markup', 'representative_image']

# pelican will ignore ipynb checkpoints
IGNORE_FILES = ['.ipynb_checkpoints']

# import pelican-theme
# THEME = "../pelican-themes/gum"
# THEME = "../pelican-themes/html5-dopetrope"
#THEME = "../pelican-themes/Flex"
THEME = "../pelican-themes/attila"
# THEME = "../pelican-themes/nest"
# THEME = "../pelican-themes/Medius"
#THEME = "../pelican-themes/bulrush"
# THEME = "../pelican-themes/pelican-striped-html5up"


# THEME = 'themes/bootstrap2'
STATIC_PATHS = ['images', 'pdfs']

OUTPUT_PATH = 'output'
PATH = 'content'


AUTHORS_BIO = {
"monica powell": {
  "name": "Monica Powell",
  "cover": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Milky_Way_Arch.jpg/1920px-Milky_Way_Arch.jpg",
  "image": "http://www.aboutmonica.com/images/monicaheadshot-bw-circlet.png",
  "website": "http://www.aboutmonica.com",
  "location": "New York City",
  "bio": "I am a web developer who enjoys tinkering with data and is passionate about making the Internet more enjoyable."
  }
}
