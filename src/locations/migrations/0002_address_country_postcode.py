# Generated by Django 3.0.2 on 2020-03-27 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country_name', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Postcode',
            fields=[
                ('postcode', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_num', models.CharField(max_length=10)),
                ('street_name', models.CharField(max_length=30)),
                ('postcode', models.ForeignKey(default='should not be null', on_delete=django.db.models.deletion.CASCADE, to='locations.Postcode')),
            ],
        ),
    ]
