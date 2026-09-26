from my_website.settings import *
from decouple import config, Csv
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

# site framework
SITE_ID = 3


#INSTALLED_APPS = []


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
# Source - https://stackoverflow.com/a/39895356
# Posted by Manoj Jadhav
# Retrieved 2026-09-13, License - CC BY-SA 3.0



if DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

else:
     DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGIN'),
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT', cast = int)
    }
}



STATIC_ROOT = BASE_DIR / "static"
MEDIA_ROOT = BASE_DIR / "media"

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]



if config('USE_SSL_SETTINGS', default=False, cast=bool):
    ## X-XSS-Protection
    SECURE_BROWSER_XSS_FILTER = True

    SCRF_COOKIE_SECURE = True
    #X-Content-Type-Options
    SECURE_CONTENT_TYPE_NOSNIFF = True
    ## Strict-Transport-Security
    SECURE_HSTS_SECONDS = 15768000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

    ## that requests over HTTP are redirected to HTTPS. aslo can config in webserver
    SECURE_SSL_REDIRECT = True 

    # for more security
    CSRF_COOKIE_SECURE = True
    CSRF_USE_SESSIONS = True
    CSRF_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_SAMESITE = 'Strict'