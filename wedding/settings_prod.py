from .settings import *

DEBUG = False
ALLOWED_HOSTS = ['wedding-production-9b77.up.railway.app']
# Database
DATABASES = {'default': dj_database_url.config(default=os.environ.get('DJANGO_DATABASE_URL'))}
# Qualquer outra configuração específica de produção
