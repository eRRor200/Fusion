# Generated by Django 3.0.6 on 2020-05-24 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scholarships', '0005_auto_20200524_1817'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Notional_prize',
            new_name='National_prize',
        ),
        migrations.AlterModelTable(
            name='national_prize',
            table='National_prize',
        ),
    ]
