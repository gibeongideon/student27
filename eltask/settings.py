"""
Django settings for eltask project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
#import dj_database_url
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-12rqgs_jnznhncse+f_qb*x4jrvw)g%a26xbi74+kx77gmed=@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [    
    #'channels',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'base',
    'home',
    'users', 
    'paypal',
    'authentication',
    'dashboard'
       

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    #'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'eltask.urls'

AUTH_USER_MODEL = "users.User"

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

WSGI_APPLICATION = 'eltask.wsgi.application'
ASGI_APPLICATION = 'eltask.asgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



#CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
#         'LOCATION': 'unix:/tmp/memcached.sock',
 #    }
#}

#CACHES = {
#    'default': {
#        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
 #       'LOCATION': 'redis://127.0.0.1:6379',
 #   }
#}

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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# The absolute path to the directory where collectstatic will collect static files for deployment.
STATIC_ROOT = BASE_DIR / 'staticfiles'

# The URL to use when referring to static files (where they will be served from)
STATIC_URL = '/static/'

# Simplified static file serving.
# https://pypi.org/project/whitenoise/
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# ManifestStaticFilesStorage is recommended in production, to prevent outdated
# JavaScript / CSS assets being served from cache (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/3.2/ref/contrib/staticfiles/#manifeststaticfilesstorage
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Heroku: Update database configuration from $DATABASE_URL.

#db_from_env = dj_database_url.config(conn_max_age=500)
#DATABASES['default'].update(db_from_env)

SITE_DOMAIN="eltask.co"


# login/logout redirect
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

JET_SIDE_MENU_COMPACT = True


# Safaricom-specific settings Configs

# B2C (Bulk Payment) Configs
# see https://developer.safaricom.co.ke/test_credentials
# https://developer.safaricom.co.ke/b2c/apis/post/paymentrequest
#SECRET_MPESA_URL=''# config("SECRET_MPESA_URL", default=SECRET_ADMIN_URL)
SECRET_MPESA_URL="h6__pz5m$yks2l93$c6ux=%!r1hm%3h%5-^$pb9wzv5^gp*@2"
MPESA_B2C_ACCESS_KEY = ''#config("MPESA_B2C_ACCESS_KEY", default="")
MPESA_B2C_CONSUMER_SECRET = ''#config("MPESA_B2C_CONSUMER_SECRET", default="")

B2C_SECURITY_TOKEN = ''#config("B2C_SECURITY_TOKEN", default="")###B1
B2C_INITIATOR_NAME =''# config("B2C_INITIATOR_NAME", default="Darius Option")###B2
B2C_COMMAND_ID = ''#config("B2C_COMMAND_ID", default="")###B3
B2C_SHORTCODE = ''#config("B2C_SHORTCODE", default="")###B4
B2C_QUEUE_TIMEOUT_URL = ''#config("B2C_QUEUE_TIMEOUT_URL", default="https://www.dariplay.ga/pesa/b2c/timeout")
B2C_RESULT_URL =''# config("B2C_RESULT_URL", default="https://www.dariplay.ga/pesa/b2c/result")
MPESA_URL = ''#config("MPESA_URL", default="https://sandbox.safaricom.co.ke")

# C2B (Paybill) Configs
# See https://developer.safaricom.co.ke/c2b/apis/post/registerurl

MPESA_C2B_ACCESS_KEY =''# config("MPESA_C2B_ACCESS_KEY", default="")
MPESA_C2B_CONSUMER_SECRET = ''#config("MPESA_C2B_CONSUMER_SECRET", default="")

C2B_REGISTER_URL = ''#config("C2B_REGISTER_URL", default="")#
C2B_VALIDATE_URL = ''#config("C2B_VALIDATE_URL", default="https://www.dariplay.ga/pesa/c2b/validate")
C2B_CONFIRMATION_URL = ''#config("C2B_CONFIRMATION_URL", default="https://www.dariplay.ga/pesa/c2b/confirmation")
C2B_SHORT_CODE =''# config("C2B_SHORT_CODE", default="")###N1
C2B_RESPONSE_TYPE = ''#config("C2B_RESPONSE_TYPE", default="Completed")
C2B_ONLINE_CHECKOUT_CALLBACK_URL = ''#"https://www.dariplay.ga/pesa/c2b/online_checkout/callback"
C2B_ONLINE_PASSKEY = ''#config("C2B_ONLINE_PASSKEY", default="")###N2
C2B_ONLINE_SHORT_CODE = ''#config("C2B_ONLINE_SHORT_CODE", default="")###N1
C2B_ONLINE_PARTY_B = ''#config("C2B_ONLINE_PARTY_B", default="")###N1

TOKEN_THRESHOLD = ''#config("TOKEN_THRESHOLD", default=600)  # , cast=int)

#Paypal


PAYPAL_BUY_BUTTON_IMAGE="https://www.paypal.com/en_US/i/btn/btn_buynowCC_LG.gif"
PAYPAL_RECEIVER_EMAIL ="emmanuel.kipyegon30@gmail.com"

PAYPAL_TEST = False


###USA/CANADA&UK

PAYPAL_WPP_USER = "sb-h2ded6675419_api1.business.example.com"

PAYPAL_WPP_PASSWORD = "DFXXXTJPDKBFA5KG"

PAYPAL_WPP_SIGNATURE = "AM1aGgn2bz5QbLwfJWgM8rQPCVdfAjz3hKc8w9Pa8XdIFnHt-9r143O2"



DJANGO_SETTINGS_MODULE = 'eltask.settings'


# Heroku: Update database configuration from $DATABASE_URL.
# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(db_from_env)



# Creating Access Token for Sandbox
PAYPAL_CLIENT_ID = ""
PAYPAL_CLIENT_SECRET =""


WHEEL_MAP = [20,6,5,0,100,50,20,0,3,2,1,0,500,0,20,10,5,0,200,25,30,0,4,2,1,0,1000,0]

