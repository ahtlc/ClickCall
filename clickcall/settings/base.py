"""
░█▀▀░█░░░▀█▀░█▀▀░█░█░█▀▀░█▀█░█░░░█░░
░█░░░█░░░░█░░█░░░█▀▄░█░░░█▀█░█░░░█░░
░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀░▀░▀▀▀░▀▀▀
Version: 0.1.0
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'users.User'

# Email config

EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get(
    'EMAIL_HOST_USER',
    'templatedmailtest@gmail.com'
)

EMAIL_HOST_PASSWORD = os.environ.get(
    'EMAIL_HOST_PASSWORD',    
    'templated@test@1234A',
)

LOGIN_REDIRECT_URL = 'users:profile'
TEMPLATED_EMAIL_BACKEND = 'templated_email.backends.vanilla_django'

# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'widget_tweaks',
]

CLICKCALL_APPS = [
    'users.apps.UsersConfig',
    'common.apps.CommonConfig',
    'calls.apps.CallsConfig',
    'activities.apps.ActivitiesConfig',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + CLICKCALL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'clickcall.urls'

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

WSGI_APPLICATION = 'clickcall.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation\
.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation\
.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation\
.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation\
.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Recife'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/staticfiles/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
