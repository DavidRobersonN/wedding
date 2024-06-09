from .settings import *
import dj_database_url

DEBUG = False
ALLOWED_HOSTS = ['wedding-production-9b77.up.railway.app']
# Database
DATABASES = {'default': dj_database_url.config(default=os.environ.get('DJANGO_DATABASE_URL'))}
# Qualquer outra configuração específica de produção
CSRF_TRUSTED_ORIGINS = ['wedding-production-9b77.up.railway.app']  # Adicione seu domínio Railway aqui