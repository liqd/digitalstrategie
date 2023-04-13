from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

try:
    import debug_toolbar
except ImportError:
    pass
else:
    INSTALLED_APPS += ("debug_toolbar",)
    MIDDLEWARE += ("debug_toolbar.middleware.DebugToolbarMiddleware",)

    INTERNAL_IPS = ("127.0.0.1", "localhost")

for template_engine in TEMPLATES:
    template_engine['OPTIONS']['debug'] = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b*1ljsb!x7@d_o$sohx-&q-7n*#r=lwhy542zxk(e=fj%ey3xp'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
CAPTCHA_URL = 'https://captcheck.netsyms.com/api.php'

try:
    from .local import *
except ImportError:
    pass

INSTALLED_APPS += ('wagtail.contrib.styleguide',)

if os.getenv("DATABASE") == "postgresql":
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '5557',
        'OPTIONS': {
            },
        }
    }
