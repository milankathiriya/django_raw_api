from django.db import models
from django.db.models.fields import DateTimeField, DecimalField

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=25)
    price = DecimalField(max_digits=10, decimal_places=2)
    created_at = DateTimeField(auto_created=True, auto_now=True)

    def __str__(self) -> str:
        return self.name + "_" + str(self.created_at)
