# Generated by Django 3.2.8 on 2021-11-23 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
