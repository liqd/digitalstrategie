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
    template_engine["OPTIONS"]["debug"] = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "b*1ljsb!x7@d_o$sohx-&q-7n*#r=lwhy542zxk(e=fj%ey3xp"


EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
CAPTCHA_URL = "https://captcha-numbers-stage.liqd.net/api.php"

try:
    from .local import *
except ImportError:
    pass

INSTALLED_APPS += ("wagtail.contrib.styleguide",)

if os.getenv("DATABASE") == "postgresql":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "django",
            "USER": "django",
            "PASSWORD": "",
            "HOST": "",
            "PORT": "5557",
            "OPTIONS": {},
        }
    }

# CSP for development (not very strict)
CSP_DEFAULT_SRC = ["'self'"]
# unsafe-eval only for testing
CSP_SCRIPT_SRC = ["'unsafe-eval'"]
CSP_SCRIPT_SRC_ATTR = ["'none'"]
# wagtail (and webpack during dev) requires unsafe-inline
CSP_SCRIPT_SRC_ELEM = [
    "'self'",
    "stats.liqd.net",
    "berlin.de",
    "www.berlin.de",
    "'unsafe-inline'",
]
CSP_IMG_SRC = [
    "'self'",
    "captcha-numbers-stage.liqd.net",
    "stats.liqd.net",
    "berlin.de",
    "www.berlin.de",
    "www.gravatar.com",
]
CSP_OBJECT_SRC = ["'none'"]
CSP_MEDIA_SRC = ["'self'"]
CSP_FRAME_SRC = [
    "'self'",
    "youtube.com",
    "www.youtube.com",
    "vimeo.com",
    "www.vimeo.com",
]
CSP_FONT_SRC = ["'self'", "berlin.de", "www.berlin.de"]
CSP_CONNECT_SRC = [
    "'self'",
    "captcha-numbers-stage.liqd.net",
    "stats.liqd.net",
    "releases.wagtail.io",
]
CSP_STYLE_SRC = ["'none'"]
# wagtail userbar requires unsafe-inline for wagtail <= 4.1
CSP_STYLE_SRC_ATTR = ["'self'", "'unsafe-inline'"]
# wagtail admin vendor.js requires unsafe-inline
CSP_STYLE_SRC_ELEM = ["'self'", "berlin.de", "www.berlin.de"]
CSP_BASE_URI = ["'self'"]
CSP_CHILD_SRC = ["'none'"]
CSP_FRAME_ANCESTORS = ["'self'"]
CSP_FORM_ACTION = ["'self'"]
CSP_MANIFEST_SRC = ["'self'"]
CSP_WORKER_SRC = ["'none'"]
CSP_EXCLUDE_URL_PREFIXES = "/admin"
CSP_REPORT_ONLY = False
