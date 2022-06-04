# Generated by Django 4.0.4 on 2022-06-03 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('document', models.IntegerField(unique=True)),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=120)),
                ('attribute', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=50, unique=True)),
                ('nit', models.IntegerField(unique=True)),
                ('code', models.IntegerField(unique=True)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Rest_API.clients')),
                ('products', models.ManyToManyField(to='Rest_API.products')),
            ],
        ),
    ]