# Generated by Django 3.0.4 on 2020-05-03 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0009_auto_20200503_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='number',
            field=models.IntegerField(default=0, verbose_name='Номер занятия'),
        ),
    ]
