# Generated by Django 3.2.6 on 2021-08-28 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='logo',
            field=models.ImageField(default=True, upload_to='media/', verbose_name='لوگو'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='home',
            name='text_button',
            field=models.CharField(default=False, max_length=30, verbose_name='متن دکمه'),
            preserve_default=False,
        ),
    ]
