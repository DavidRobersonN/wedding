PROJETO WEB SITE WEDDING
""""""""

Após criar o projeto no pycharme, fazer a instalação de algumas bibliotecas:
    pip install django psycopg2-binary gunicorn dj-static django-stdimage

Em seguida, vamos criar o arquivo requirements
    pip freeze > requirements.txt

Criando o Projeto:
    django-admin startproject wedding

Criando a aplicação:
    django-admin startapp core

Alterar algumas configurações em setting
    ALLOWED_HOSTS = ["*"]

    INSTALLED_APPS = [
    'core',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    ]

    'DIRS': ['templates'],

    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'wedding',
        'USER': 'david',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432'
        }
    }

    STATIC_URL = 'static/'
    MEDIA_URL = 'media/'
    STATIC_URL = os.path.join(BASE_DIR, 'staticfiles')
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

alterar o arquivo wedding.urls.py

    from django.contrib import admin
    from django.urls import path, include
    from django.conf.urls.static import static
    from django.conf import settings

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('core.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

alterar o arquivo core.urls 
    from django.urls import path
    from . views import IndexView

    urlpatterns = [
        path('', IndexView.as_view(), name='index')
    ]

Começar editando os arquivos html, fazendo alterações para poder usar os arquivos estaticos, por exemplo deve ficar desta forma:

    <link rel="stylesheet" href="{% static 'css/style.css' %}">

Precisa tambem colocar o seguinte codigo no cabeçado da pagina, para eu possa carregar os arquivos estaticos:
    {% load static %}

