# Generated by Django 5.0.4 on 2024-04-17 14:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_noivo_remove_people_tipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noiva',
            fields=[
                ('people_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.people')),
                ('bio', models.TextField(max_length=200, verbose_name='Bio')),
            ],
            options={
                'abstract': False,
            },
            bases=('core.people',),
        ),
    ]
