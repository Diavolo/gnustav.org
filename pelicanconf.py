#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from datetime import date

AUTHOR = 'Diavolo'
SITENAME = 'GNUstav'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Lima'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TAG_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('FreeBSD', 'https://www.freebsd.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('github', 'https://github.com/Diavolo'),
          ('diaspora', 'https://diasp.eu/u/diavolo'),
          ('pump.io', 'https://identi.ca/diavolo'),
          ('mastodon', 'https://mastodon.social/users/Diavolo'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
# ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'
PAGE_URL = 'p/{slug}.html'
PAGE_SAVE_AS = 'p/{slug}.html'

THEME = "../../Templates/pelican/nest"

# custom page generated with a jinja2 template
# TEMPLATE_PAGES = {'jinja2/404.html': '404.html',}

# static paths will be copied without parsing their contents
STATIC_PATHS = [
    'extra',
    'images',
    'media',
    ]

# path-specific metadata
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    # 'extra/404.html': {'path': '404.html'},
    'images/favicon.ico': {'path': 'favicon.ico'},
    'images/logo.svg': {'path': 'logo.svg'},
    }

TYPOGRIFY = True
TYPOGRIFY_IGNORE_TAGS = ['code', 'pre']

TAGLINE = "De Software Libre"
SITESUBTITLE = TAGLINE

PLUGIN_PATHS = ['../../Templates/pelican-plugins']
PLUGINS = ['sitemap', 'liquid_tags.youtube']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.9,
        'indexes': 0.5,
        'pages': 0.3
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}


# Minified CSS
NEST_CSS_MINIFY = True
# Add items to top menu before pages
MENUITEMS = [
    ('Home', '/'),
    ('About', 'https://gahd.net')
    ]
# Add header background image from content/images : 'background.jpg'
NEST_HEADER_IMAGES = ''
NEST_HEADER_LOGO = '/logo.svg'
# Footer
NEST_SITEMAP_COLUMN_TITLE = 'Sitemap'
NEST_SITEMAP_MENU = [
    ('Archives', '/archives.html'),
    ('Categories', '/categories.html'),
    ('Tags', '/tags.html')
    ]
NEST_SITEMAP_ATOM_LINK = 'Atom Feed'
NEST_SITEMAP_RSS_LINK = 'RSS Feed'
NEST_SOCIAL_COLUMN_TITLE = 'Social'
NEST_LINKS_COLUMN_TITLE = 'Links'
NEST_COPYRIGHT = '&copy; GNUstav Huarcaya ' + str(date.today().year)
# Footer optional
NEST_FOOTER_HTML = ''
# index.html
NEST_INDEX_HEAD_TITLE = 'M-x butterfly'
NEST_INDEX_HEADER_TITLE = 'GNUstav'
NEST_INDEX_HEADER_SUBTITLE = TAGLINE
NEST_INDEX_CONTENT_TITLE = 'Last Posts'
# archives.html
NEST_ARCHIVES_HEAD_TITLE = 'Archives'
NEST_ARCHIVES_HEAD_DESCRIPTION = 'Posts Archives'
NEST_ARCHIVES_HEADER_TITLE = 'Archives'
NEST_ARCHIVES_HEADER_SUBTITLE = 'Archives for all posts'
NEST_ARCHIVES_CONTENT_TITLE = 'Archives'
# article.html
NEST_ARTICLE_HEADER_BY = 'By'
NEST_ARTICLE_HEADER_MODIFIED = 'modified'
NEST_ARTICLE_HEADER_IN = 'in category'
# author.html
NEST_AUTHOR_HEAD_TITLE = 'Posts by'
NEST_AUTHOR_HEAD_DESCRIPTION = 'Posts by'
NEST_AUTHOR_HEADER_SUBTITLE = 'Posts archives'
NEST_AUTHOR_CONTENT_TITLE = 'Posts'
# authors.html
NEST_AUTHORS_HEAD_TITLE = 'Author list'
NEST_AUTHORS_HEAD_DESCRIPTION = 'Author list'
NEST_AUTHORS_HEADER_TITLE = 'Author list'
NEST_AUTHORS_HEADER_SUBTITLE = 'Archives listed by author'
# categories.html
NEST_CATEGORIES_HEAD_TITLE = 'Categories'
NEST_CATEGORIES_HEAD_DESCRIPTION = 'Archives listed by category'
NEST_CATEGORIES_HEADER_TITLE = 'Categories'
NEST_CATEGORIES_HEADER_SUBTITLE = 'Archives listed by category'
# category.html
NEST_CATEGORY_HEAD_TITLE = 'Category Archive'
NEST_CATEGORY_HEAD_DESCRIPTION = 'Category Archive'
NEST_CATEGORY_HEADER_TITLE = 'Category'
NEST_CATEGORY_HEADER_SUBTITLE = 'Category Archive'
# pagination.html
NEST_PAGINATION_PREVIOUS = 'Previous'
NEST_PAGINATION_NEXT = 'Next'
# period_archives.html
NEST_PERIOD_ARCHIVES_HEAD_TITLE = 'Archives for'
NEST_PERIOD_ARCHIVES_HEAD_DESCRIPTION = 'Archives for'
NEST_PERIOD_ARCHIVES_HEADER_TITLE = 'Archives'
NEST_PERIOD_ARCHIVES_HEADER_SUBTITLE = 'Archives for'
NEST_PERIOD_ARCHIVES_CONTENT_TITLE = 'Archives for'
# tag.html
NEST_TAG_HEAD_TITLE = 'Tag archives'
NEST_TAG_HEAD_DESCRIPTION = 'Tag archives'
NEST_TAG_HEADER_TITLE = 'Tag'
DiavoloNEST_TAG_HEADER_SUBTITLE = 'Tag archives'
# tags.html
NEST_TAGS_HEAD_TITLE = 'Tags'
NEST_TAGS_HEAD_DESCRIPTION = 'Tags List'
NEST_TAGS_HEADER_TITLE = 'Tags'
NEST_TAGS_HEADER_SUBTITLE = 'Tags List'
NEST_TAGS_CONTENT_TITLE = 'Tags List'
NEST_TAGS_CONTENT_LIST = 'tagged'
