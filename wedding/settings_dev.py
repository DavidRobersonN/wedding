from .settings import *

DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1:8000']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'wedding',
        'USER': 'postgres',
        'PASSWORD': '159635',
        'HOST': 'localhost',
        'PORT': '5433',
    }
}
# Qualquer outra configuração específica de desenvolvimento
