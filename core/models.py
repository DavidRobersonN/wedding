from django.db import models
import uuid
from stdimage.models import StdImageField
from datetime import datetime

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Base(models.Model):
    nome = models.CharField('Nome', max_length=100)
    imagem = StdImageField('Imagem', upload_to=get_file_path,
                           variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})

    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        abstract = True


class Padrinho(Base):
    CHOICES = (
        ('noivo', 'noivo'),
        ('noiva', 'noiva'),
    )
    ladoFamilia = models.CharField('ladoFamilia', max_length=12, choices=CHOICES)
    def __str__(self):
        return self.nome

class Noivo(Base):
    bio = models.TextField('Bio', max_length=200)

    def __str__(self):
        return self.nome

class Noiva(Base):
    bio = models.TextField('Bio', max_length=200)

    def __str__(self):
        return self.nome
