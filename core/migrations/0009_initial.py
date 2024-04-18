# Generated by Django 5.0.4 on 2024-04-18 13:35

import core.models
import stdimage.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0008_remove_noivo_people_ptr_remove_padrinho_people_ptr_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Padrinho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('imagem', stdimage.models.StdImageField(force_min_size=False, upload_to=core.models.get_file_path, variations={'thumb': {'crop': True, 'height': 480, 'width': 480}}, verbose_name='Imagem')),
                ('facebook', models.CharField(default='#', max_length=100, verbose_name='Facebook')),
                ('twitter', models.CharField(default='#', max_length=100, verbose_name='Twitter')),
                ('instagram', models.CharField(default='#', max_length=100, verbose_name='Instagram')),
                ('ladoFamilia', models.CharField(choices=[('noivo', 'noivo'), ('noiva', 'noiva')], max_length=5, verbose_name='ladoFamilia')),
            ],
            options={
                'verbose_name': 'Padrinho',
                'verbose_name_plural': 'Padrinhos',
            },
        ),
    ]