from .base import *

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
DEBUG = False

INSTALLED_APPS += ['wagtail.contrib.postgres_search']

DATABASES = {
'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'django',
    'USER': 'django',
    'PASSWORD': '',
    'HOST': '',
    'PORT': '',
    'OPTIONS': {
        },
    }
}

try:
    from .local import *
except ImportError:
    pass
