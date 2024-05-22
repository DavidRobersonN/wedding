# Generated by Django 5.0.4 on 2024-05-21 00:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_noivo_noiva'),
    ]

    operations = [
        migrations.AddField(
            model_name='noiva',
            name='noivo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='noiva_relacionada', to='core.noivo'),
        ),
        migrations.AlterField(
            model_name='noivo',
            name='noiva',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='noivo_relacionado', to='core.noiva'),
        ),
    ]
