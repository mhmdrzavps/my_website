from my_website.settings import *
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-6neb7ina37=@in2-f7ws32%4=+$s2dx16zov$xeoyhk=x0dpe0"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['travelista.ir', 'www.travelista.ir']

# site framework
SITE_ID = 3


#INSTALLED_APPS = []


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

# Source - https://stackoverflow.com/a/39895356
# Posted by Manoj Jadhav
# Retrieved 2026-09-13, License - CC BY-SA 3.0



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'travelis_travel',
        'USER': 'travelis_mohamadreza',
        'PASSWORD': 'UbC$$hc;Ek+4]p;+',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}



STATIC_ROOT = BASE_DIR / "static"
MEDIA_ROOT = BASE_DIR / "MEDIA"

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]


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