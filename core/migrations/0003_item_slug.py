# Generated by Django 2.2.10 on 2020-05-09 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200509_0135'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(default='test-product'),
            preserve_default=False,
        ),
    ]
