# Generated by Django 2.1.2 on 2019-01-26 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0003_auto_20190126_1906'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request_to_lease_offer',
            old_name='Request_to_lease',
            new_name='request_to_lease',
        ),
    ]