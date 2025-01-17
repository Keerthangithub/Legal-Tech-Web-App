"""
Django settings for legaltech project.

Generated by 'django-admin startproject' using Django 4.1.8.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--5s6l+yhupph%yb98s&2g6^%ve070#$u#the74o$wz5j)90i#)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    "whitenoise.runserver_nostatic",
    'django.contrib.staticfiles',
    #  'djongo',
    # 'allauth',
    # 'allauth.account',
    # 'allauth.socialaccount',
    # 'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.github',
    'accounts',
    "home",
    "client",
    "lsp",
    "admin_app",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Add the account middleware:
    # "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = 'legaltech.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
                'django.template.context_processors.request',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    # 'allauth.account.auth_backends.AuthenticationBackend',
   
]


#SITE_ID=1
# 240318269996-2ujo6ujdtq45cukgergu7qn7vdfk8idi.apps.googleusercontent.com
# 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

WSGI_APPLICATION = 'legaltech.wsgi.app'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

import dj_database_url

DATABASES = {
    # 'default': dj_database_url.parse('postgresql://postgres:dC4GCC-6g3Efg3FFBGffcC6cCbG*-BCC@roundhouse.proxy.rlwy.net:21684/railway')
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',  # Use your local database engine
    #     'NAME': BASE_DIR / "db.sqlite3",  # Adjust the path as needed
    # },
     'default': dj_database_url.parse('postgres://crazycoders:MkaIZ4K82Qf4FsK8DmXcFeZ2CAIM2vaw@dpg-cm8p4p6d3nmc73b0dojg-a.oregon-postgres.render.com/pec_render_database'),
    # 'default': dj_database_url.parse('postgres://crazycoders:MkaIZ4K82Qf4FsK8DmXcFeZ2CAIM2vaw@dpg-cm8p4p6d3nmc73b0dojg-a.oregon-postgres.render.com/pec_render_database')
    # 'default': dj_database_url.parse('postgres://crazycoders:MkaIZ4K82Qf4FsK8DmXcFeZ2CAIM2vaw@dpg-cm8p4p6d3nmc73b0dojg-a.oregon-postgres.render.com/pec_render_database')
    
}




# DATABASES={
#     "default": dj_database_url.parse(os.environ.get("DATABASE_URL"))
# }





# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'

# At the end of file. add these lines

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build','static') # here static is like assets
MEDIA_URLS ='/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Also Make aure To set allowed_hosts to '*'

# CRISPY_TEMPLATE_PACK = 'bootstrap4'
STATICFILES_DIRS=[
    os.path.join(BASE_DIR, 'static')
]


SITE_ID = 1

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')


# STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage" 

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER ='crazycodersdev@gmail.com'
EMAIL_HOST_PASSWORD ='uxllkibqnucpbraa'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_TIMEOUT = None

STATICFILES_STORAGE='django.contrib.staticfiles.storage.ManifestStaticFilesStorage'


# from decouple import config

# OPENAI_API_KEY = config('OPENAI_API_KEY')


# LOGIN_REDIRECT_URL = 'home'

# ACCOUNT_LOGOUT_REDIRECT_URL = 'user_login'

# ACCOUNT_EMAIL_REQUIRED = True

# SOCIALACCOUNT_QUERY_EMAIL = True

# ACCOUNT_SESSION_REMEMBER = True

# SOCIALACCOUNT_PROVIDERS = {
#     'facebook': {
#         'METHOD': 'oauth2',
#         'SDK_URL': '//connect.facebook.net/{locale}/sdk.js',
#         'SCOPE': ['email', 'public_profile'],
#         'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
#         'INIT_PARAMS': {'cookie': True},
#         'FIELDS': [
#             'id',
#             'first_name',
#             'last_name',
#             'middle_name',
#             'name',
#             'name_format',
#             'picture',
#             'short_name'
#         ],
#         'EXCHANGE_TOKEN': True,
#         # 'LOCALE_FUNC': 'path.to.callable',
#         'VERIFIED_EMAIL': False,
#         'VERSION': 'v7.0',
#     }
# }



# STORAGES = {
    
#     "staticfiles": {
#         "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
#     },
# }