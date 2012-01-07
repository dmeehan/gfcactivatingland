# Django settings for gfcactivatingland.org.

import os

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
SITE_ROOT = os.path.join(PROJECT_DIR, os.pardir, os.pardir)
PROJECT_URL = '/'

DEBUG = True
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
MEDIA_URL = '/media/uploads/'

STATIC_ROOT = os.path.join(SITE_ROOT, 'media/', 'static/')
STATIC_URL = '/media/static/'

# ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]

STATICFILES_STORAGE = 'staticfiles.storage.StaticFileStorage'

STATICFILES_FINDERS = (
   'staticfiles.finders.FileSystemFinder',
   'staticfiles.finders.AppDirectoriesFinder',
)


#==============================================================================
# Templates
#==============================================================================

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)


TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.request",
    "grappelli.context_processors.admin_template_path",
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
    'staticfiles.context_processors.static',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)


#==============================================================================
# Middleware
#==============================================================================


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.csrf.CsrfMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.csrf.CsrfResponseMiddleware',
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
    'staticfiles',

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
COMMENTS_MODERATE_AFTER = 0
COMMENTS_CLOSE_AFTER = 0

# Profile settings
AUTH_PROFILE_MODULE = "accounts.UserProfile"


#==============================================================================
# Third party app settings
#==============================================================================


# Grappelli Settings
GRAPPELLI_ADMIN_TITLE = 'Grounds for Change'


# Admin Tools Settings
ADMIN_TOOLS_MENU = 'gfcactivatingland.menu.CustomMenu'
ADMIN_TOOLS_INDEX_DASHBOARD = 'gfcactivatingland.dashboard.CustomIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'gfcactivatingland.dashboard.CustomAppIndexDashboard'

# Haystack settings
HAYSTACK_SITECONF = 'gfcactivatingland.search_sites'
HAYSTACK_SEARCH_ENGINE = 'simple'

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