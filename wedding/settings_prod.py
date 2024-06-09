from .settings import *
import dj_database_url

DEBUG = False
ALLOWED_HOSTS = ['wedding-production-9b77.up.railway.app', 'wedding-production-9b77.up.railway.app/admin']
# Database
DATABASES = {'default': dj_database_url.config(default=os.environ.get('DJANGO_DATABASE_URL'))}
# Qualquer outra configuração específica de produção
