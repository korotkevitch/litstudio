# Generated by Django 3.0.2 on 2020-10-15 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stihinazakaz', '0016_feedback2_how_many'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback2',
            name='message',
        ),
        migrations.AddField(
            model_name='feedback2',
            name='deadline',
            field=models.CharField(blank=True, max_length=50, verbose_name='Срок написания стихов'),
        ),
        migrations.AddField(
            model_name='feedback2',
            name='special',
            field=models.CharField(blank=True, max_length=300, verbose_name='Особые пожелания к стихам'),
        ),
    ]
