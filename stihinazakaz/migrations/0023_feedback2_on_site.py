# Generated by Django 3.0.2 on 2020-10-18 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stihinazakaz', '0022_auto_20201016_0725'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback2',
            name='on_site',
            field=models.CharField(blank=True, choices=[('one', 'От одного человека'), ('few', 'От нескольких')], max_length=3),
        ),
    ]