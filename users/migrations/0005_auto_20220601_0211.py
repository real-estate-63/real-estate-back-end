# Generated by Django 3.2.12 on 2022-06-01 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='realestate',
            name='address',
        ),
        migrations.AddField(
            model_name='address',
            name='real_estate',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='address_real_estate', to='users.realestate'),
        ),
    ]
