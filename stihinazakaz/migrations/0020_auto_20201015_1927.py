# Generated by Django 3.0.2 on 2020-10-15 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stihinazakaz', '0019_auto_20201015_1922'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback2',
            options={'verbose_name': 'Заказ на стихи', 'verbose_name_plural': 'Заказ на стихи'},
        ),
        migrations.AlterField(
            model_name='feedback2',
            name='about',
            field=models.TextField(blank=True, verbose_name='О нем'),
        ),
        migrations.AlterField(
            model_name='feedback2',
            name='adresat',
            field=models.CharField(blank=True, max_length=500, verbose_name='О нём'),
        ),
        migrations.AlterField(
            model_name='feedback2',
            name='age',
            field=models.CharField(blank=True, max_length=50, verbose_name='Лет'),
        ),
        migrations.AlterField(
            model_name='feedback2',
            name='deadline',
            field=models.CharField(blank=True, max_length=50, verbose_name='Срок'),
        ),
        migrations.AlterField(
            model_name='feedback2',
            name='kem_prihodit',
            field=models.CharField(blank=True, max_length=50, verbose_name='Кем приходится'),
        ),
        migrations.AlterField(
            model_name='feedback2',
            name='special',
            field=models.CharField(blank=True, max_length=300, verbose_name='Особые пожелания'),
        ),
        migrations.AlterField(
            model_name='feedback2',
            name='wishes',
            field=models.CharField(blank=True, max_length=300, verbose_name='Пожелания'),
        ),
    ]
