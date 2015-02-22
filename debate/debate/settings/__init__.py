"""
Django settings for debate project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
here = lambda *x: os.path.realpath(os.path.join(BASE_DIR, *x))


SECRET_KEY = '#yg4vpbht$iszj#&oi!lz4ynu0+bk+!*l1ec+izubq_05f-4qz'
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'debate.base',
    'social.apps.django_app.default',
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
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'social.backends.facebook.FacebookOAuth2',
)
SOCIAL_AUTH_FACEBOOK_KEY = os.getenv('FB_KEY', '')
SOCIAL_AUTH_FACEBOOK_SECRET = os.getenv('FB_SECRET', '')
FACEBOOK_SCOPE = 'email,publish_stream'

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details'
)

ROOT_URLCONF = 'debate.urls'
WSGI_APPLICATION = 'debate.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "base/js"),
]

STATIC_URL = '/static/'
STATIC_ROOT = 'static'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'debate',
        # The following settings are not used with sqlite3:
        'USER': os.getenv('DB_USER', 'debate'),
        'PASSWORD': os.getenv('DB_PASS', 'debate'),
        'HOST': os.getenv("DB_HOST", 'localhost'),
        'PORT': os.getenv('DB_PORT', ''),
    }
}

REST_FRAMEWORK = {
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    # ]
}
