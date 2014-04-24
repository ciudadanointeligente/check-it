"""
Django settings for deldichoalhecho_site project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^5(h974)gqu+-q%m+0gyp(io2=%(qa=9pb4outi=riv$o_lyzg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'south',
    'taggit',
    'popolo',
    'constance',
    'constance.backends.database',
    'django_extensions',
    'django_nose',
    'deldichoalhecho',
    'deldichoalhecho_web',
    'deldichoalhecho_theme',
    'popit'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'deldichoalhecho_site.urls'

WSGI_APPLICATION = 'deldichoalhecho_site.wsgi.application'

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

SITE_ID = 1

USE_TZ = True

SOUTH_TESTS_MIGRATE = False

SOUTH_MIGRATION_MODULES = {
    'taggit': 'taggit.south_migrations',
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

#CONSTANCE
CONSTANCE_CONFIG = {
        'LANDING_PHRASE': ("Del dicho al hecho punto ce ele", 'the landing phrase for the site'),
}
CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'
TEMPLATE_CONTEXT_PROCESSORS = ("django.contrib.auth.context_processors.auth",
                               "django.core.context_processors.debug",
                               "django.core.context_processors.i18n",
                               "django.core.context_processors.media",
                               "django.core.context_processors.static",
                               "django.core.context_processors.tz",
                               "django.contrib.messages.context_processors.messages",
                               "constance.context_processors.config")
#HEROKU SPECIFICS
# Parse database configuration from $DATABASE_URL
if 'DATABASE_URL' in os.environ:
    import dj_database_url
    DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'


STATICFILES_DIRS = (
        os.path.join(BASE_DIR, '..', 'deldichoalhecho_web', 'static'),
        os.path.join(BASE_DIR, '..', ' deldichoalhecho_theme', 'static'),
)

# END OF HEROKU SPECIFICS
