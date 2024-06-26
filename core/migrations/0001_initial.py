# Generated by Django 5.0.6 on 2024-06-23 23:58

import core.models
import datetime
import django.db.models.deletion
import stdimage.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Casamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataCerimonia', models.DateField(verbose_name='Data da Cerimonia')),
                ('endereco', models.CharField(blank=True, max_length=255, null=True)),
                ('horaInicioCerimonia', models.TimeField(blank=True, default=datetime.time(12, 0), null=True)),
                ('horaTerminoCerimonia', models.TimeField(blank=True, default=datetime.time(12, 0), null=True)),
                ('horaInicioFesta', models.TimeField(blank=True, default=datetime.time(12, 0), null=True)),
                ('horaTerminoFesta', models.TimeField(blank=True, default=datetime.time(12, 0), null=True)),
                ('biografiaCasal', models.CharField(blank=True, max_length=255, null=True)),
                ('mensagemCerimonia', models.CharField(blank=True, max_length=255, null=True)),
                ('mensagemFesta', models.CharField(blank=True, max_length=255, null=True)),
                ('textoApresentacaoBlog', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'verbose_name': 'Casamento',
                'verbose_name_plural': 'Casamentos',
            },
        ),
        migrations.CreateModel(
            name='Convidados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome')),
                ('imagem', stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to=core.models.get_file_path, variations={'thumb': {'crop': True, 'height': 480, 'width': 480}}, verbose_name='Imagem')),
                ('facebook', models.CharField(default='#', max_length=100, verbose_name='Facebook')),
                ('twitter', models.CharField(default='#', max_length=100, verbose_name='Twitter')),
                ('instagram', models.CharField(default='#', max_length=100, verbose_name='Instagram')),
            ],
            options={
                'verbose_name': 'Convidado',
                'verbose_name_plural': 'Convidados',
            },
        ),
        migrations.CreateModel(
            name='Noiva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome')),
                ('imagem', stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to=core.models.get_file_path, variations={'thumb': {'crop': True, 'height': 480, 'width': 480}}, verbose_name='Imagem')),
                ('facebook', models.CharField(default='#', max_length=100, verbose_name='Facebook')),
                ('twitter', models.CharField(default='#', max_length=100, verbose_name='Twitter')),
                ('instagram', models.CharField(default='#', max_length=100, verbose_name='Instagram')),
                ('bio', models.TextField(default='', max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Noiva',
                'verbose_name_plural': 'Noivas',
            },
        ),
        migrations.CreateModel(
            name='NossoBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome')),
                ('imagem', stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to=core.models.get_file_path, variations={'thumb': {'crop': True, 'height': 480, 'width': 480}}, verbose_name='Imagem')),
                ('facebook', models.CharField(default='#', max_length=100, verbose_name='Facebook')),
                ('twitter', models.CharField(default='#', max_length=100, verbose_name='Twitter')),
                ('instagram', models.CharField(default='#', max_length=100, verbose_name='Instagram')),
                ('titulo', models.CharField(blank=True, max_length=50, null=True)),
                ('texto', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
            },
        ),
        migrations.CreateModel(
            name='HistoriaDeAmor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome')),
                ('imagem', stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to=core.models.get_file_path, variations={'thumb': {'crop': True, 'height': 480, 'width': 480}}, verbose_name='Imagem')),
                ('facebook', models.CharField(default='#', max_length=100, verbose_name='Facebook')),
                ('twitter', models.CharField(default='#', max_length=100, verbose_name='Twitter')),
                ('instagram', models.CharField(default='#', max_length=100, verbose_name='Instagram')),
                ('titulo', models.CharField(max_length=100)),
                ('conteudo', models.TextField()),
                ('casamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historias', to='core.casamento')),
            ],
            options={
                'verbose_name': 'História de Amor',
                'verbose_name_plural': 'Histórias de Amor',
            },
        ),
        migrations.CreateModel(
            name='Madrinha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome')),
                ('imagem', stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to=core.models.get_file_path, variations={'thumb': {'crop': True, 'height': 480, 'width': 480}}, verbose_name='Imagem')),
                ('facebook', models.CharField(default='#', max_length=100, verbose_name='Facebook')),
                ('twitter', models.CharField(default='#', max_length=100, verbose_name='Twitter')),
                ('instagram', models.CharField(default='#', max_length=100, verbose_name='Instagram')),
                ('noiva', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='madrinhas', to='core.noiva')),
            ],
            options={
                'verbose_name': 'Madrinha',
                'verbose_name_plural': 'Madrinhas',
            },
        ),
        migrations.CreateModel(
            name='Noivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome')),
                ('imagem', stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to=core.models.get_file_path, variations={'thumb': {'crop': True, 'height': 480, 'width': 480}}, verbose_name='Imagem')),
                ('facebook', models.CharField(default='#', max_length=100, verbose_name='Facebook')),
                ('twitter', models.CharField(default='#', max_length=100, verbose_name='Twitter')),
                ('instagram', models.CharField(default='#', max_length=100, verbose_name='Instagram')),
                ('bio', models.TextField(default='', max_length=100, null=True)),
                ('noiva', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='noivo_relacionado', to='core.noiva')),
            ],
            options={
                'verbose_name': 'Noivo',
                'verbose_name_plural': 'Noivos',
            },
        ),
        migrations.AddField(
            model_name='noiva',
            name='noivo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='noiva_relacionada', to='core.noivo'),
        ),
        migrations.AddField(
            model_name='casamento',
            name='noivo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='casamentos', to='core.noivo'),
        ),
        migrations.CreateModel(
            name='Padrinho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome')),
                ('imagem', stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to=core.models.get_file_path, variations={'thumb': {'crop': True, 'height': 480, 'width': 480}}, verbose_name='Imagem')),
                ('facebook', models.CharField(default='#', max_length=100, verbose_name='Facebook')),
                ('twitter', models.CharField(default='#', max_length=100, verbose_name='Twitter')),
                ('instagram', models.CharField(default='#', max_length=100, verbose_name='Instagram')),
                ('noivo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='padrinhos', to='core.noivo')),
            ],
            options={
                'verbose_name': 'Padrinho',
                'verbose_name_plural': 'Padrinhos',
            },
        ),
        migrations.CreateModel(
            name='Saudacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conteudo', models.TextField(blank=True, null=True)),
                ('saudacaoNoiva', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saudacaoNoiva', to='core.noiva')),
                ('saudacaoNoivo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saudacaoNoivo', to='core.noivo')),
            ],
            options={
                'verbose_name': 'Saudação',
                'verbose_name_plural': 'Saudações',
            },
        ),
    ]
