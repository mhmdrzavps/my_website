from my_website.settings import *
from decouple import config , Csv
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# site framework
SITE_ID = 2


#INSTALLED_APPS = [  ]


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }


STATIC_ROOT = BASE_DIR / "static"
MEDIA_ROOT = BASE_DIR / "media"

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

X_FRAME_OPTIONS = "SAMEORIGIN"
