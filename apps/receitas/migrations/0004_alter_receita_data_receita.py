# Generated by Django 3.2.5 on 2021-07-19 12:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0003_auto_20210719_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='data_receita',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 19, 9, 32, 25, 444244)),
        ),
    ]