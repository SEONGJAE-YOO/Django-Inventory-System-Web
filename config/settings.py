"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
from re import S

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e0pf0ws@7ijrxzbftvuh)zri43-cjb6)s@$(!($ryu&g^f!c4='

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
    'django.contrib.staticfiles',
    'dashboard.apps.DashboardConfig',
    'user.apps.UserConfig',
    'crispy_forms',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DjangoInventorySystemWeb',
        'USERNAME': 'YooSeongJae',
        'HOST': 'django-inventory-system-web.c238yawlhe0h.ap-northeast-2.rds.amazonaws.com',
        'PORT': 3306,
        'PASSWORD': 'tjdwo357!',  # Your Password
    }
}
#한국 리전을 AWS 는 "ap-northeast-2"
'''
AZ 정보는 아래와 같이 리전코드의 뒤에 붙여 표현합니다. a zone, b zone, c zone 을 보유하는 서울리전은 아래처럼 표기합니다.

ap-northeast-2a    ap-northeast-2c    ap-northeast-2b(오픈한지 얼마 안됐습니다.)   
 
저는 ap-northeast-2b으로 설정하였습니다.

모든 사용자에게 가용영역 a, b, c 가 같은 가용영역은 아닙니다.

말이 좀 어려운데, 예를들어 A 사용자의  a 가용영역이 "용인" 센터라면, B 사용자의 a 가용영역은 "서울" 센터일 수도 있습니다. 아무래도 한 가용영역에 리소스가 몰리는 것을 방지하기 위해서입니다. 
'''
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

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'


STATTICFILES_DIRS = [
    BASE_DIR / "static"
]

STATIC_ROOT = (BASE_DIR/"asert/")

MEDIA_ROOT = (BASE_DIR/'media')

MEDIA_URL = '/media/'


LOGIN_REDIRECT_URL = 'dashboard-index'

LOGIN_URL = 'user-login'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST ='smtp.gmail.com'
EMAIL_PORT = 587

EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'yousong4243123@gmail.com'
EMAIL_HOST_PASSWORD = 'tjdwo357!!!'
