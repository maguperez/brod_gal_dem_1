"""
Django settings for broderjobs project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from unipath import Path
RUTA_PROYECTO=Path(__file__).ancestor(2)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f6x=__b=u%r1^czhr#-)tmh%ur*o%w(knn0!jg8l1fxu3oc44q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'django.contrib.postgres',
    'crispy_forms',
    'main',
    'estudiante',
    'empresa',
    'oportunidad',
    'endless_pagination',
    'mensaje',
    'contador_visitas',
    'disc',
    'cultura_empresarial',


)

CRISPY_TEMPLATE_PACK = 'bootstrap3'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'social.apps.django_app.middleware.SocialAuthExceptionMiddleware',
)

ROOT_URLCONF = 'broderjobs.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            'django.core.context_processors.request',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request',
                'estudiante.context_processors.estudiante_foto',
                'estudiante.context_processors.notificaciones',
                # 'cultura_empresarial.context_processors.calcular_cultura_empresa',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'broderjobs.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

if 'RDS_DB_NAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'BroderJobs1',
            'USER': 'broder',
            'PASSWORD': 'br753des',
            'HOST': '191.168.19.11',
            'PORT': '5434',
        }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'es-ES'

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DATE_INPUT_FORMATS = [
    '%d/%m/%Y',              # '10/25/2006'
    '%d/%m/%Y %H:%M:%S',     # '10/25/2006 14:30:59'
    '%d/%m/%Y %H:%M:%S.%f',  # '10/25/2006 14:30:59.000200'
    '%d/%m/%Y %H:%M',        # '10/25/2006 14:30'
    '%d/%m/%y %H:%M:%S',     # '10/25/06 14:30:59'
    '%d/%m/%y %H:%M:%S.%f',  # '10/25/06 14:30:59.000200'
    '%d/%m/%y %H:%M',        # '10/25/06 14:30'
    '%d/%m/%y',              # '10/25/06'
    '%Y-%m-%d %H:%M:%S',     # '2006-10-25 14:30:59'
    '%Y-%m-%d %H:%M:%S.%f',  # '2006-10-25 14:30:59.000200'
    '%Y-%m-%d %H:%M',        # '2006-10-25 14:30'
    '%Y-%m-%d',              # '2006-10-25'
]

from django.core.urlresolvers import reverse_lazy
LOGIN_URL = reverse_lazy('homepage')
LOGIN_REDIRECT_URL = reverse_lazy('oportunidades')
LOGOUT_URL = reverse_lazy('logout')


if 'RDS_DB_NAME' in os.environ:

    AWS_HEADERS = {  # see http://developer.yahoo.com/performance/rules.html#expires
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
            'Cache-Control': 'max-age=94608000',
    }

    AWS_STORAGE_BUCKET_NAME = 'broderjobs'
    AWS_ACCESS_KEY_ID = 'AKIAJB4CICGN7PI5OWNA'
    AWS_SECRET_ACCESS_KEY = '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'

    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

    STATICFILES_LOCATION = 'static'

    STATICFILES_STORAGE = 'broderjobs.custom_storages.StaticStorage'

    STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

    STATIC_ROOT = os.path.join(BASE_DIR, "..", "www", "static")

    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "static"),
    #    '/BroderJobs/broderjobs/static/',
    )

    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    )

else:
    STATIC_ROOT = ''
    STATIC_URL = '/static/'
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "static"),
        '/BroderJobs/broderjobs/static/',
    )
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    )

if 'RDS_DB_NAME' in os.environ:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIAFILES_LOCATION = 'media'
    MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
    DEFAULT_FILE_STORAGE = 'broderjobs.custom_storages.MediaStorage'
else:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'


#Social-Autt
#variable


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'social.backends.facebook.FacebookAppOAuth2',
    'social.backends.facebook.FacebookOAuth2',
    'broderjobs.backends.EmailOrUsernameModelBackend',
)

EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'info@broderjobs.com'
SERVER_EMAIL = 'info@broderjobs.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'info@broderjobs.com'
EMAIL_HOST_PASSWORD = 'infbrodperu123'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


SOCIAL_AUTH_PIPELINE = (
    # 'social.pipeline.social_auth.social_details',
    # 'social.pipeline.social_auth.social_uid',
    # 'social.pipeline.social_auth.auth_allowed',
    # 'social.pipeline.social_auth.social_user',
    # 'social.pipeline.user.get_username',
    # 'social.pipeline.user.create_user',
    # 'social.pipeline.social_auth.associate_user',
    # 'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'broderjobs.utils.associate_by_email',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'broderjobs.utils.crear_estudiante'
)

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/login-facebook/'

SOCIAL_AUTH_FACEBOOK_KEY = '963480823713807'
SOCIAL_AUTH_FACEBOOK_SECRET = '7119ba6ba620df948721cb20fc9189cc'

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id,name,email',
}