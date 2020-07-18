from .base import *

DEBUG = False
COMPRESS_ENABLED = True

SECRET_KEY = 'kjfasjijlkj242345löjk2h4jh32jh542jk2lj4hx'

ALLOWED_HOSTS = ['siedler.co', 'www.siedler.co', '64.227.113.104']

try:
    from .local import *
except ImportError:
    pass
