# Generated by Django 2.1 on 2018-08-19 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='let_equipment',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/equipment'),
        ),
    ]
