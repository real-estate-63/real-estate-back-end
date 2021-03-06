# Generated by Django 3.2.12 on 2022-06-03 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('slug', models.CharField(max_length=128)),
                ('type', models.CharField(max_length=64)),
                ('name_with_type', models.CharField(max_length=64)),
                ('code', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'country',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('slug', models.CharField(max_length=128)),
                ('type', models.CharField(max_length=64)),
                ('name_with_type', models.CharField(max_length=64)),
                ('code', models.CharField(max_length=64)),
                ('parent_code', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'district',
            },
        ),
        migrations.CreateModel(
            name='ProvinceCity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('slug', models.CharField(max_length=128)),
                ('type', models.CharField(max_length=64)),
                ('name_with_type', models.CharField(max_length=64)),
                ('code', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'province_city',
            },
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('slug', models.CharField(max_length=128)),
                ('type', models.CharField(max_length=64)),
                ('name_with_type', models.CharField(max_length=64)),
                ('code', models.CharField(max_length=64)),
                ('parent_code', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'ward',
            },
        ),
    ]
