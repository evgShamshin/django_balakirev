# Generated by Django 5.1.7 on 2025-04-18 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website_app', '0010_tag_alter_command_options_command_tag'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='command',
            options={'ordering': ('pk',)},
        ),
    ]
