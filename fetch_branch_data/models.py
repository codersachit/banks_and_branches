from django.db import models

# Create your models here.

class Bank(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=49)

class Branch(models.Model):
    ifsc = models.CharField(max_length=11)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    branch = models.CharField(max_length=74)
    address = models.CharField(max_length=195)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=26)



