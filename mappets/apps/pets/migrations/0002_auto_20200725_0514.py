# Generated by Django 2.2.13 on 2020-07-25 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specie',
            name='breed',
        ),
        migrations.AddField(
            model_name='breed',
            name='specie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='breeds', to='pets.Specie'),
        ),
    ]
