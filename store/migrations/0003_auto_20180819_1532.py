# Generated by Django 2.1 on 2018-08-19 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20180819_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store_item',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]