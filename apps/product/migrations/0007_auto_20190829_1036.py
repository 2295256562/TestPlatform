# Generated by Django 2.2.2 on 2019-08-29 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20190829_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='creater_time',
            field=models.BigIntegerField(default=1567046195, verbose_name='创建时间'),
        ),
    ]
