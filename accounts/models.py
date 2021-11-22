from django.db import models


class Customer(models.Model):
    ID = models.IntegerField(primary_key=True)
    Nume = models.CharField(max_length=255, null=True)
    Prenume = models.CharField(max_length=255, null=True)
    Email = models.CharField(max_length=255, null=True)
    Password = models.CharField(max_length=255, null=True)
    PhoneNumber = models.CharField(max_length=12, null=True)
    Username = models.CharField(max_length=255, null=True)

