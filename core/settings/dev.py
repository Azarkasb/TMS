from .base import *
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
# SECURITY
SECRET_KEY = 'scatman'

DEBUG = True

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "myproject",
        "USER": "myprojectuser",
        "PASSWORD": 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# Default primary key field type

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CACHES = {
    "default": {
        "BACKEND": 'django.core.cache.backends.memcached.MemcachedCache',
        "LOCATION": "127.0.0.1:11211"
    }
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename':'tms.log',
            'formatter': 'app',
            # 'filename': '/var/log/tms.log'
        }
    },
    'loggers': {
        'tms': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
    "formatters": {
        "app": {
            "format": (
                u"%(asctime)s [%(levelname)-8s] "
                "(%(module)s.%(funcName)s) %(message)s"
            ),
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
}
