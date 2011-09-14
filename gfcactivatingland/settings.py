# Django settings for gfcactivatingland.org.

import os

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
SITE_ROOT = os.path.join(PROJECT_DIR, os.pardir)
PROJECT_URL = '/'

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Douglas Meehan', 'dmeehan@gmail.com'),
)

MANAGERS = ADMINS

SITE_ID = 1

#==============================================================================
# Localization
#==============================================================================

TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
USE_I18N = False    #internationalization machinery
USE_L10N = True    #format dates, numbers and calendars according to locale


#==============================================================================
# Project URLS and media settings
#==============================================================================

ROOT_URLCONF = 'gfcactivatingland.urls'

MEDIA_ROOT = os.path.join(SITE_ROOT, 'media/', 'uploads/')
MEDIA_URL = '/uploads/'

STATIC_ROOT = os.path.join(SITE_ROOT, 'media/', 'static/')
STATIC_URL = '/static/'

# ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


#==============================================================================
# Templates
#==============================================================================

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.i18n",
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
)

# TEMPLATE_CONTEXT_PROCESSORS += (
    # 'Custom context processors here',
# )

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#   'django.template.loaders.eggs.Loader',
)

#==============================================================================
# Middleware
#==============================================================================


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)


#==============================================================================
# Installed Apps
#==============================================================================

INSTALLED_APPS = (
    # third party admin apps. Must go first.
    'grappelli',
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',

    # contrib
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.markup',
    'django.contrib.comments',

    # third party apps
    'south',
    'tagging',
    'imagekit',
    'flatblocks',
    'haystack',
    'profiles',
    'registration',
    'uni_form',

    # actionmanual apps
    'actionmanual.categories',
    'actionmanual.sections',
    'actionmanual.contacts',
    'actionmanual.portfolio',
    'actionmanual.posts',
    'actionmanual.resources',
    'actionmanual.accounts',

)


#==============================================================================
# Django app settings
#==============================================================================


# Comments settings
COMMENTS_AKISMET_API_KEY = '7cbaf5969a99'
COMMENTS_MODERATE_AFTER = 30
COMMENTS_CLOSE_AFTER = 0

# Profile settings
AUTH_PROFILE_MODULE = "accounts.UserProfile"


#==============================================================================
# Third party app settings
#==============================================================================


# Grappelli Settings
GRAPPELLI_ADMIN_TITLE = 'Grounds for Change'


# Admin Tools Settings
ADMIN_TOOLS_MENU = 'actionmanual.menu.CustomMenu'
ADMIN_TOOLS_INDEX_DASHBOARD = 'actionmanual.dashboard.CustomIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'actionmanual.dashboard.CustomAppIndexDashboard'

# Haystack settings
HAYSTACK_SITECONF = 'actionmanual.search_sites'
HAYSTACK_SEARCH_ENGINE = 'simple'
HAYSTACK_WHOOSH_PATH = '/home/cityparks/webapps/actionmanual_django/whoosh/actionmanual_index'

# registation settings
ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window

# Google Maps settings
MAPS_API_KEY = 'ABQIAAAAayJegR1S7-F1AMio1LsppBQxMADg_4nSozIzUm9-z1HndOaHgxQZcIZevol--KGWt42h3WLWcr2a5Q'


#==============================================================================
# Local app settings
#==============================================================================


# actionmanual.posts settings
PORTFOLIO_MARKUP = 'markdown'

POSTS_MARKUP = 'markdown'


#==============================================================================
# local environment settings
#==============================================================================

try:
    from local_settings import *
except ImportError:
    pass