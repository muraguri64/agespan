# Generated by Django 2.1.2 on 2018-12-08 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer_transport_request',
            name='status',
            field=models.CharField(choices=[('approved', 'APPROVED'), ('pending', 'PENDING')], default='pending', max_length=255),
        ),
        migrations.AlterField(
            model_name='request_transport_offer',
            name='status',
            field=models.CharField(choices=[('approved', 'APPROVED'), ('pending', 'PENDING')], default='pending', max_length=255),
        ),
    ]
