# Generated by Django 3.0.6 on 2020-05-27 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capp', '0002_auto_20200527_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='css',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='css/'),
        ),
    ]
