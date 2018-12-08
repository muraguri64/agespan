# Generated by Django 2.1.2 on 2018-12-08 15:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('regions', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crops', '0002_crop_type_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buy_Land',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(max_length=255)),
                ('price_per', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('approved', 'APPROVED'), ('pending', 'PENDING')], default='pending', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Lease_Let_Land',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('price_per', models.CharField(max_length=255)),
                ('lease_period', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('approved', 'APPROVED'), ('pending', 'PENDING')], default='pending', max_length=255)),
                ('crop_to_grow', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='crops.Crop_Type')),
            ],
        ),
        migrations.CreateModel(
            name='Let_Land',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('land_size', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('nearest_town', models.CharField(max_length=255)),
                ('water_source', models.CharField(choices=[('groundwater', 'GROUNDWATER'), ('river', 'RIVER'), ('lake', 'LAKE'), ('reservoir', 'RESERVOIR'), ('none', 'NONE')], default='none', max_length=255)),
                ('lease_period', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('price_per', models.CharField(max_length=255)),
                ('owner_name', models.CharField(max_length=255)),
                ('owner_email', models.CharField(max_length=255)),
                ('owner_contact', models.CharField(max_length=255)),
                ('available', models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], default='yes', max_length=255)),
                ('crop_grown', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='crops.Crop_Type')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='regions.Region')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Request_To_Buy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('land_size', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('nearest_town', models.CharField(max_length=255)),
                ('price_range', models.CharField(max_length=255)),
                ('price_range_per', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='regions.Region')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Request_To_Buy_Offers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('price_per', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('approved', 'APPROVED'), ('pending', 'PENDING')], default='pending', max_length=255)),
                ('request_to_buy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='land.Request_To_Buy')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Request_To_Lease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('land_size', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('nearest_town', models.CharField(max_length=255)),
                ('lease_period', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('price_per', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='regions.Region')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Request_To_Lease_Offers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('price_per', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('approved', 'APPROVED'), ('pending', 'PENDING')], default='pending', max_length=255)),
                ('Request_to_lease', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='land.Request_To_Lease')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sell_Land',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('land_size', models.CharField(max_length=255)),
                ('specific_location', models.CharField(max_length=255)),
                ('nearest_town', models.CharField(max_length=255)),
                ('price_range', models.CharField(max_length=255)),
                ('price_per', models.CharField(max_length=255)),
                ('owner_name', models.CharField(max_length=255)),
                ('owner_email', models.CharField(max_length=255)),
                ('owner_contact', models.CharField(max_length=255)),
                ('available', models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], default='yes', max_length=255)),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='regions.Region')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='lease_let_land',
            name='let_land',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='land.Let_Land'),
        ),
        migrations.AddField(
            model_name='lease_let_land',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='buy_land',
            name='sell_land',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='land.Sell_Land'),
        ),
        migrations.AddField(
            model_name='buy_land',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
