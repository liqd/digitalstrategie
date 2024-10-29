from .base import *

DEBUG = False

STORARGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    },
}


try:
    from .local import *
except ImportError:
    pass
