# Generated by Django 3.2.5 on 2021-07-21 17:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0009_auto_20210721_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='data_receita',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 21, 14, 43, 30, 549264)),
        ),
    ]
