# Generated by Django 5.0.6 on 2024-05-24 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='categoria',
            field=models.CharField(choices=[('0', 'WINE AND BEER'), ('1', 'COCKTAILS')], max_length=1, verbose_name='Categoria'),
        ),
    ]
