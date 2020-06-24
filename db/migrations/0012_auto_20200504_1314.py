# Generated by Django 3.0.4 on 2020-05-04 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0011_auto_20200503_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacttype',
            name='function',
            field=models.CharField(blank=True, max_length=255, verbose_name='Функция'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='billingDate',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата выставления'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='receiptDate',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата получения'),
        ),
    ]
