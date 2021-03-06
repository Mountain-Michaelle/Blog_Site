"""
Django settings for Blog project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""


from pathlib import Path


import django_heroku
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '045cd087a91c04359b9bda8035081929197444884db64ec8'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True
ALLOWED_HOSTS = ['https://git.heroku.com/murmuring-river-00434.git', '127.0.0.1']
SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    #Django default application
    'account.apps.AccountConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
     # My own applications...
    'blogs.apps.BlogsConfig',
    'social_django',
    'images.apps.ImagesConfig',
    # Django third-party apps.
    'taggit',
    # Sitemap app recctifiers 
    'django.contrib.sites',
    'django.contrib.sitemaps',
    # djanog postgresql databases
    'django.contrib.postgres',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]


ROOT_URLCONF = 'Blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '41240075',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
"""


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Settings for email backends 
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_PASSWORD = 'mypassword'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False


"""# Email settings
EMAIL_HOST = 'localhost'
EMAIL_HOST_USER = 'mony@monycell.com'
EMAIL_HOST_PASSWORD = 'mypassword'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False
"""
LOGIN_URL = 'account:login'
LOGIN_REDIRECT_URL = 'account:dashboard'
LOGOUT_URL = 'account:logout'


AUTHENTICATION_BACKEND = [
    'django.contrib.auth.backends.ModelBackend',
    'account.authenticatetion.EmailAuthBackend',
    'social_core.backends.facebook.FacebookOAuth2',
]

# Setting for heroku deployments
django_heroku.settings(locals())
SOCIAL_AUTH_FACEBOOK_KEY = '1185000272250134dd' #Facebook App ID
SOCIAL_AUTH_FACEBOOK_SECRET = ''