# Generated by Django 3.0.2 on 2020-10-15 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stihinazakaz', '0010_auto_20201015_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback2',
            name='you',
            field=models.CharField(choices=[('ty', 'Ты'), ('vy', 'Вы')], max_length=2),
        ),
    ]
