# Generated by Django 2.2.7 on 2019-11-19 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20191119_1835'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Usuário', 'verbose_name_plural': 'Users'},
        ),
    ]