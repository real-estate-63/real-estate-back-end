# Generated by Django 3.2.12 on 2022-06-01 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_address_real_estate'),
    ]

    operations = [
        migrations.AddField(
            model_name='realestate',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.userprofile'),
            preserve_default=False,
        ),
    ]