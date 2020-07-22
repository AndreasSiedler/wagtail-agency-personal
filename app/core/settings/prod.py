from .base import *

DEBUG = False
COMPRESS_ENABLED = True
SECRET_KEY = 'kjfasjijlkj242345löjk2h4jh32jh542jk2lj4hx'

ALLOWED_HOSTS = ['siedler.co', 'www.siedler.co', '64.227.113.104']

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

try:
    from .local import *
except ImportError:
    pass
