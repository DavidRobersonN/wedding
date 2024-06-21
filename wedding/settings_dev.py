from .settings import *

DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'wedding',
        'USER': 'postgres',
        'PASSWORD': os.environ.get('DJANGO_KEY_DATABASES_LOCAL'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
# Qualquer outra configuração específica de desenvolvimento
