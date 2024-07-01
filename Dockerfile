# Use a imagem oficial do Python como base
FROM python:3.11.4

# Instalar o Nginx
RUN apt-get update && apt-get install -y nginx

# Configurações do Django
ENV PYTHONUNBUFFERED 1
WORKDIR /app

# Copiar os arquivos do projeto para o contêiner
COPY . /app/

# Instalar as dependências do Django
RUN pip install -r requirements.txt

# Copiar a configuração do Nginx para o contêiner
COPY nginx.conf /etc/nginx/nginx.conf

# Coletar os arquivos estáticos
RUN python manage.py collectstatic --noinput

# Comandos para iniciar o servidor Django e o Nginx
CMD service nginx start && gunicorn wedding.wsgi:application --bind 0.0.0.0:8000
