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

# Pagination
DEFAULT_PAGINATION = 3
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)


# Post and Pages path
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Tags and Category path
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORIES_SAVE_AS = 'catgegories.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_SAVE_AS = 'tags.html'

# Author
AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHORS_SAVE_AS = 'authors.html'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# render ipynb as markdown
MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup', 'neighbors', 'sitemap']
# old plugin ==> ,'minchin.pelican.plugins.cname'

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

STATIC_PATHS = ['images', 'pdfs',  'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

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

# Sitemap
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
