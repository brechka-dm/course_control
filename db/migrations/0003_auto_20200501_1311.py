# Generated by Django 3.0.4 on 2020-05-01 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_destribution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
    ]
