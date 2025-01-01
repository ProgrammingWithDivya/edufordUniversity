"""
Django settings for university project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')


#SECRET_KEY = 'django-insecure-(0z7--ps(n2vc=@f%*pk5=jr%d&c8&8ftd6*(566a&#^8t8nq*'

# SECURITY WARNING: don't run with debug turned on in production!
# Debug mode (change based on environment)
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Use environment variable for ALLOWED_HOSTS
ALLOWED_HOSTS = ['eduforduniversity-l0so.onrender.com', 'localhost', '127.0.0.1']

#ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

# Ensure that the ALLOWED_HOSTS is set correctly
if not ALLOWED_HOSTS:
    raise ValueError("ALLOWED_HOSTS is not set properly in the .env file!")

#ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = [
    'https://eduforduniversity-l0so.onrender.com',  # Add your domain here
    'https://your-other-trusted-domain.com',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'universityapp',
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

ROOT_URLCONF = 'university.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'university.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
import os
import dj_database_url

# Load environment variables from .env file
load_dotenv()
# Load environment variables from the .env file located in the root of the project
dotenv_path = Path(__file__).resolve().parent.parent / '.env'  # Path to .env in the root
load_dotenv(dotenv_path=dotenv_path)

DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL')
    )
}


'''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),  # Reads DB_NAME from environment variable
        'USER': os.environ.get('DB_USER'),  # Reads DB_USER from environment variable
        'PASSWORD': os.environ.get('DB_PASSWORD'),  # Reads DB_PASSWORD from environment variable
        'HOST': os.environ.get('DB_HOST'),  # Reads DB_HOST from environment variable
        'PORT': os.environ.get('DB_PORT', '5432'),  # Default to 5432 if not set
    }
}'''


'''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres123',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}'''


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/
import os
from pathlib import Path

# Get the base directory path
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "universityapp" / "static",  # Correct path to the static directory
]

STATIC_ROOT = BASE_DIR/'staticfiles'


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# settings.py

# Make sure you have this enabled
SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # or choose another backend if needed

# The session cookie name and age can be adjusted as needed
SESSION_COOKIE_AGE = 60 * 60 * 24  # 1 day (in seconds)

CSRF_COOKIE_SECURE = False 
CSRF_COOKIE_HTTPONLY = False 
CSRF_COOKIE_SAMESITE = 'Lax'
