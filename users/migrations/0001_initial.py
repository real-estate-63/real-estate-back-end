# Generated by Django 3.2.12 on 2022-06-02 18:01

from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('systems', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('user_type', models.IntegerField(choices=[(1, 'Sell'), (2, 'Buy')], null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'users',
            },
            managers=[
                ('objects', users.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('full_name', models.CharField(max_length=150)),
                ('phone_number', models.CharField(max_length=14)),
                ('birth_date', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_profile',
            },
        ),
        migrations.CreateModel(
            name='RealEstate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('type', models.IntegerField(choices=[(1, 'Sell'), (2, 'Lease')], default=1)),
                ('price', models.FloatField()),
                ('area', models.FloatField()),
                ('description', models.TextField()),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('status', models.IntegerField(choices=[(1, 'New'), (2, 'Sold')], default=1)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.userprofile')),
                ('type_lease', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='systems.typelease')),
                ('type_sell', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='systems.typesell')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'real_estate',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_street', models.CharField(max_length=64)),
                ('number', models.CharField(max_length=5)),
                ('full_address', models.CharField(max_length=256)),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='systems.country')),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='systems.district')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address_profile', to='users.userprofile')),
                ('province_city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='systems.provincecity')),
                ('real_estate', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='address_real_estate', to='users.realestate')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ward', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='systems.ward')),
            ],
            options={
                'db_table': 'address',
            },
        ),
    ]
