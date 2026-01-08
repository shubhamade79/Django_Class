from django.db import models

# Create your models here.

class Punejob(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=25)
    title = models.CharField(max_length=25)
    address = models.CharField(max_length=100)
    salary = models.IntegerField(max_length=20)
    email = models.EmailField(max_length=20)
    phone = models.BigIntegerField(max_length=20)


class BangJob(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=25)
    title = models.CharField(max_length=25)
    address = models.CharField(max_length=100)
    salary = models.IntegerField(max_length=20)
    email = models.EmailField(max_length=20)
    phone = models.BigIntegerField(max_length=20)


class BiharJob(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=25)
    title = models.CharField(max_length=25)
    address = models.CharField(max_length=100)
    salary = models.IntegerField(max_length=20)
    email = models.EmailField(max_length=20)
    phone = models.BigIntegerField(max_length=20)