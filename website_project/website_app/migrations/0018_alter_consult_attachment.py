# Generated by Django 5.1.7 on 2025-05-23 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_app', '0017_consult'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consult',
            name='attachment',
            field=models.FileField(blank=True, upload_to='website_app/atachment'),
        ),
    ]
