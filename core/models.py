from django.db import models
import uuid
from stdimage.models import StdImageField

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

class Noiva(Base):
    bio = models.TextField(max_length=100, null=True, default='')

    class Meta:
        verbose_name = 'Noiva'
        verbose_name_plural = 'Noivas'

    def __str__(self):
        return self.nome

class Noivo(Base):
    bio = models.TextField(max_length=100, null=True, default='')
    noiva = models.OneToOneField(Noiva, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Noivo'
        verbose_name_plural = 'Noivos'

    def __str__(self):
        return self.nome

class Madrinha(Base):
    nome = models.CharField('Nome', max_length=100)

    class Meta:
        verbose_name = 'Madrinha'
        verbose_name_plural = 'Madrinhas'

    def __str__(self):
        return self.nome

class Padrinho(Base):
    nome = models.CharField('Nome', max_length=100)

    class Meta:
        verbose_name = 'Madrinha'
        verbose_name_plural = 'Madrinhas'

    def __str__(self):
        return self.nome
