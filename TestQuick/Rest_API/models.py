from django.db import models

# Create your models here.


class Clients(models.Model):
    id = models.AutoField(primary_key=True)
    document = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=120, null=False)
    last_name = models.CharField(max_length=120, null=False)
    email = models.EmailField(unique=True)

    objects = models.Manager()


class Products(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=120)
    attribute = models.IntegerField()

    objects = models.Manager()


class Bills(models.Model):
    id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey(Clients, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50, null=False, unique=True)
    nit = models.IntegerField(unique=True)
    code = models.IntegerField(unique=True)
    products = models.ManyToManyField(Products)

    objects = models.Manager()
