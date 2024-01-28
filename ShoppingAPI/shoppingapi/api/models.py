# api/models.py
from django.db import models

class ShoppingItem(models.Model):
    name = models.CharField(max_length=255)
    bought = models.BooleanField(default=False)

    def __str__(self):
        return self.name
