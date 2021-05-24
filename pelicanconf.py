#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from datetime import datetime

# Basic Settings
PATH = 'content'
ARTICLE_PATHS = ['articles']
# STATIC_PATHS = ["images"]
SITEURL = 'http://127.0.0.1:8000'
SITENAME = 'Y.Y.Blog'
SUMMARY_MAX_LENGTH = 5
PYGMENTS_RST_OPTIONS = {
  'linenos': 'table',
}
PLUGIN_PATHS = ['plugins']
PLUGINS = ['related_posts',
           'share_post',
           'neighbors',
           'sitemap',
           'tipue_search',]
RELATED_POSTS_MAX = 5
SITEMAP = {
    'format': 'xml'}
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'search']

# URL Settings
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'
YEAR_ARCHIVE_URL = 'posts/{date:%Y}/'
YEAR_ARCHIVE_SAVE_AS =  'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_URL = 'posts/{date:%Y}/{date:%m}/'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'
SLUGIFY_SOURCE = 'basename'

# Time and Date
TIMEZONE = 'Asia/Tokyo'
DEFAULT_DATE='fs'
DEFAULT_DATE_FORMAT = '%Y/%m/%d'

# META DATA
AUTHOR = 'yy'

# Feed Settings
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Translations
DEFAULT_LANG = 'Japanese'

# Theme
THEME = 'themes/Flex'
SITESUBTITLE = "Y.Y.Blog"
# GITHUB_URL = 'https://github.com/yamaccu'
MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
)
# LINKS = ()
SOCIAL = (('twitter', 'https://twitter.com/YY87750722'),
          ("github", "https://github.com/yamaccu"))

# Pagination
DEFAULT_PAGINATION = 10


# FLEX Settings
# 上部のタグ
MAIN_MENU = True

# メニューの丸アイコン
SITELOGO = SITEURL+"/images/profile.png"

# Path to favicon.ico
FAVICON = SITEURL+"/images/profile.ico"

# Code Highlight style
PYGMENTS_STYLE = "monokai"

#	If True hide URL hash.
DISABLE_URL_HASH = True

# ページ下部にライセンス表記を追加
CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike 4.0 International License",
    "version": "4.0",
    "slug": "by-sa",
}
COPYRIGHT_YEAR = datetime.now().year

# Use LESS files instead of CSS (avoid on production, it's for testing purpose)
USE_LESS = True 