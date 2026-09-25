from my_website.settings import *
from decouple import config , Csv
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = []

# site framework
SITE_ID = 2


#INSTALLED_APPS = [  ]


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

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
MEDIA_ROOT = BASE_DIR / "MEDIA"

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

X_FRAME_OPTIONS = "SAMEORIGIN"
