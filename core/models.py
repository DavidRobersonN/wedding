import datetime
from django.db import models
import uuid
from stdimage.models import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    nome = models.CharField('Nome', max_length=100, null=True,
                            blank=True)
    imagem = StdImageField('Imagem', upload_to=get_file_path,
                           variations={'thumb': {'width': 480, 'height': 480, 'crop': True}}, null=True,
                           blank=True)
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        abstract = True


class Noiva(Base):
    bio = models.TextField(max_length=100, null=True, default='')
    noivo = models.ForeignKey('Noivo', on_delete=models.CASCADE, related_name='noiva_relacionada', null=True,
                              blank=True)

    class Meta:
        verbose_name = 'Noiva'
        verbose_name_plural = 'Noivas'

    def __str__(self):
        return self.nome


class Noivo(Base):
    bio = models.TextField(max_length=100, null=True, default='')
    noiva = models.ForeignKey('Noiva', on_delete=models.CASCADE, related_name='noivo_relacionado', null=True,
                              blank=True)

    class Meta:
        verbose_name = 'Noivo'
        verbose_name_plural = 'Noivos'

    def __str__(self):
        return self.nome


class Madrinha(Base):
    noiva = models.ForeignKey('Noiva', on_delete=models.CASCADE, related_name='madrinhas', null=True)

    class Meta:
        verbose_name = 'Madrinha'
        verbose_name_plural = 'Madrinhas'

    def __str__(self):
        return self.nome


class Padrinho(Base):
    noivo = models.ForeignKey('Noivo', on_delete=models.CASCADE, related_name='padrinhos', null=True)

    class Meta:
        verbose_name = 'Padrinho'
        verbose_name_plural = 'Padrinhos'

    def __str__(self):
        return self.nome


class Casamento(models.Model):
    noivo = models.ForeignKey(Noivo, on_delete=models.CASCADE, related_name='casamentos')
    dataCerimonia = models.DateField(verbose_name='Data da Cerimonia')
    endereco = models.CharField(max_length=255, blank=True, null=True)  # Campo para endereço
    horaInicioCerimonia = models.TimeField(default=datetime.time(12, 0), blank=True, null=True)
    horaTerminoCerimonia = models.TimeField(default=datetime.time(12, 0), blank=True, null=True)
    horaInicioFesta = models.TimeField(default=datetime.time(12, 0), blank=True, null=True)
    horaTerminoFesta = models.TimeField(default=datetime.time(12, 0), blank=True, null=True)
    biografiaCasal = models.CharField(max_length=255, blank=True, null=True)
    mensagemCerimonia = models.CharField(max_length=255, blank=True, null=True)
    mensagemFesta = models.CharField(max_length=255, blank=True, null=True)
    textoApresentacaoBlog = models.CharField(max_length=250, blank=True, null=True)

    def get_dia_da_semana(self):
        dias_da_semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado',
                          'Domingo']
        return dias_da_semana[self.dataCerimonia.weekday()]

    class Meta:
        verbose_name = 'Casamento'
        verbose_name_plural = 'Casamentos'

    def __str__(self):
        return f'Casamento de {self.noivo.nome}'


class HistoriaDeAmor(Base):
    casamento = models.ForeignKey(Casamento, on_delete=models.CASCADE, related_name='historias')
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()

    class Meta:
        verbose_name = 'História de Amor'
        verbose_name_plural = 'Histórias de Amor'

    def __str__(self):
        return self.titulo


class Saudacao(models.Model):
    saudacaoNoivo = models.ForeignKey(Noivo, on_delete=models.CASCADE, related_name='saudacaoNoivo', null=True,
                                      blank=True)
    saudacaoNoiva = models.ForeignKey(Noiva, on_delete=models.CASCADE, related_name='saudacaoNoiva', null=True,
                                      blank=True)
    conteudo = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Saudação'
        verbose_name_plural = 'Saudações'

    def __str__(self):
        if self.saudacaoNoivo:
            return self.saudacaoNoivo.nome
        elif self.saudacaoNoiva:
            return self.saudacaoNoiva.nome


class NossoBlog(Base):
    titulo = models.CharField(max_length=50, blank=True, null=True)
    texto = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return self.titulo


class Convidados(Base):

    class Meta:
        verbose_name = 'Convidado'
        verbose_name_plural = 'Convidados'

    def __str__(self):
        return self.nome
