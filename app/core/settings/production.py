from .base import *

DEBUG = False
SECRET_KEY = 't-zl$)!^dhh$kiz8-)!rr02t8uhn4%v6nl*f*y62p9xmxy94dh'

ALLOWED_HOSTS = ['*']

# EMAIL SETTINGS
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'andreas.siedler@gmail.com'
EMAIL_HOST_PASSWORD = '!Andi_89'

## Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'debug.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# Compressor SETTINGS
STATICFILES_FINDERS += ['compressor.finders.CompressorFinder',]

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True

COMPRESS_URL = STATIC_URL
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter'
]
COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.JSMinFilter',
]
COMPRESS_STORAGE = 'compressor.storage.GzipCompressorFileStorage' 



try:
    from .local import *
except ImportError:
    pass
