# Generated by Django 5.1.7 on 2025-05-01 18:08

import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_app', '0011_alter_command_options'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='command',
            managers=[
                ('published', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='command',
            name='is_published',
            field=models.BooleanField(choices=[(0, 'В разработке'), (1, 'Опубликовано')], default=0),
        ),
    ]
