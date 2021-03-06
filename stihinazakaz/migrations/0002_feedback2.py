# Generated by Django 3.0.2 on 2020-10-15 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stihinazakaz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holiday', models.CharField(max_length=50, verbose_name='С каким праздником поздравляем')),
                ('name', models.CharField(max_length=50, verbose_name='Ваше имя')),
                ('tel', models.CharField(max_length=50, verbose_name='Телефон')),
                ('Email', models.EmailField(max_length=50, verbose_name='Емейл')),
                ('message', models.CharField(max_length=500, verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Сообщение пользователя',
                'verbose_name_plural': 'Сообщения пользователей',
            },
        ),
    ]
