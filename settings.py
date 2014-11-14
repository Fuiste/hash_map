"""
Django settings for django_full_embretard project.

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
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'YOU DID NOT ENTER A SECRET KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INTERNAL_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'custom_user',
    'rest_framework'
)

EXTERNAL_APPS = (
    'session',
    'app'
)

AUTH_USER_MODEL = 'custom_user.EmailUser'

INSTALLED_APPS = INTERNAL_APPS + EXTERNAL_APPS

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_RENDERER_CLASSES': (
        'djangorestframework_camel_case.render.CamelCaseJSONRenderer', # Any other renders
    ),
    'DEFAULT_PARSER_CLASSES': (
        'djangorestframework_camel_case.parser.CamelCaseJSONParser', # Any other parsers
    ),
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'middleware.warning_exception_middleware.ProcessExceptionMiddleware',
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'django_full_embretard.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'NAME': os.environ.get('DB_NAME', '******** YOUR DB NAME HERE ********'),
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': os.environ.get('POSTGRES_DB_USER', '******** YOUR DB USER HERE ********'),
        'PASSWORD': os.environ.get('POSTGRES_DB_PASS', '******** YOUR DB PASSWORD HERE ********'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# Allow all host headers
ALLOWED_HOSTS = ["*"]

# Static asset configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = "staticfiles"

PROJECT_ROOT = os.path.dirname(__file__)
TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, "templates"),
)

if DEBUG:
    STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static/static_serve/')

STATIC_URL = os.environ.get("DJANGO_STATIC_URL", "/static/")

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
