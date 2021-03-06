# Generated by Django 3.2.5 on 2021-07-19 13:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0006_auto_20210719_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='data_receita',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 19, 10, 39, 12, 747747)),
        ),
        migrations.AlterField(
            model_name='receita',
            name='foto_receita',
            field=models.ImageField(blank=True, height_field=200, upload_to='fotos/%d/%m/%Y/', width_field=340),
        ),
    ]
