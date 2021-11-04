from django.db import models


class Customer(models.Model):
    id = models.IntegerField()
    nume = models.CharField(max_length=255, null=True)
    prenume = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255, null=True)
    phoneNumber = models.CharField(max_length=12, null=True)
    username = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.username
