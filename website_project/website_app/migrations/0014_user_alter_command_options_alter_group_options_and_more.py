# Generated by Django 5.1.7 on 2025-05-02 09:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_app', '0013_alter_command_options_alter_command_managers'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('is_staff', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterModelOptions(
            name='command',
            options={'ordering': ('pk',), 'verbose_name': 'Команда', 'verbose_name_plural': 'Команды'},
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ('pk',), 'verbose_name': 'Группа', 'verbose_name_plural': 'Группы'},
        ),
        migrations.AlterField(
            model_name='command',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='command',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='website_app.group', verbose_name='Группа'),
        ),
        migrations.AlterField(
            model_name='command',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='command',
            name='is_published',
            field=models.IntegerField(choices=[(0, 'В разработке'), (1, 'Опубликовано')], default=0, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='command',
            name='link',
            field=models.URLField(blank=True, verbose_name='Документация'),
        ),
        migrations.AlterField(
            model_name='command',
            name='slug',
            field=models.SlugField(blank=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='command',
            name='tag',
            field=models.ManyToManyField(blank=True, to='website_app.tag', verbose_name='Тэг'),
        ),
        migrations.AlterField(
            model_name='command',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Команда'),
        ),
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.SlugField(blank=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='group',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Группа'),
        ),
    ]
