"""
Django settings for itmemory project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from os.path import join

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')_cvtcgaa17)$*spo83$^ozn0j5j0g983ey3-)b_3xh5806ds%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'admin_tools',
    'grappelli.dashboard',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django_ftpserver',
    'django_mailbox',
    'chartit',
    'sbadmin2',
    'jquery',
    'crispy_forms',
    'dbbackup',
    'cron',
    'djfrontend',
    'djfrontend.skeleton',
    'home',
    'customers',
    'objects',
    'ittasks',
    'hwlogs',
    'hpilo',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'itmemory.urls'

WSGI_APPLICATION = 'itmemory.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'itmemory',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',  # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    },
}
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'it-it'

TIME_ZONE = 'Europe/Rome'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.tz"
)

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
# STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, "static"),
#)

DJFRONTEND_STATIC_URL = '/static/'

# ADMIN_TOOLS_MENU = 'itmemory.menu.CustomMenu'

LOGIN_URL = 'mysite_login'
LOGOUT_URL = 'mysite_logout'
LOGIN_REDIRECT_URL = '/'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

GRAPPELLI_INDEX_DASHBOARD = 'custom_dashboard.CustomIndexDashboard'
GRAPPELLI_ADMIN_TITLE = "It Memory Administration"

#MAGONET IMPORTER

MAGONETDB = {
    'server': 'SQLSERVERHOST.domain.local',
    'port': '1433',
    'user': 'sa',
    'password': 'sa',
    'db': 'DB_NET',
}

# MAIL TEPLATED
TEMPLATED_EMAIL_BACKEND = 'templated_email.backends.vanilla_django.TemplateBackend'
EMAIL_HOST = '127.0.0.1'
EMAIL_PORT = 25
EMAIL_SENDER = 'mail@example.com'

# HPILO
HPILO_OLD_STATUS = 7

# IMPOSTAZIONI NOTIFICA TASK
TASK_REMIND_DAYS = 2
TASK_EXPIRED_DAYS = 2
TASK_PRE_EXPIRED_DAYS = 1

if not os.path.exists(join(BASE_DIR, "logs")):
    os.makedirs(join(BASE_DIR, "logs"))

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'filename': join(BASE_DIR, "logs/logs.log"),
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'D',
            'interval': 1,
            'backupCount': 0,
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

try:
    from settings_local import *
except ImportError:
    pass