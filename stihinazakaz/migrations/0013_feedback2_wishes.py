# Generated by Django 3.0.2 on 2020-10-15 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stihinazakaz', '0012_feedback2_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback2',
            name='wishes',
            field=models.CharField(blank=True, max_length=100, verbose_name='Ваши пожелания'),
        ),
    ]
