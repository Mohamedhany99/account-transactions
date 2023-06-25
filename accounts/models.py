from django.db import models


class Account(models.Model):
    id = models.AutoField(primary_key=True)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
