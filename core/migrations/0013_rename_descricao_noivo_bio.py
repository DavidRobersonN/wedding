# Generated by Django 5.0.4 on 2024-04-18 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_noivo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='noivo',
            old_name='descricao',
            new_name='bio',
        ),
    ]