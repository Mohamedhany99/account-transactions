from django.db import models
from uuid import uuid4


class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100, null=True, blank=True)
    balance = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self) -> str:
        return self.name
