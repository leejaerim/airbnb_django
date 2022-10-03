from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
 # 데이터의 모양을 장고에게 알려줌.
class House(models.Model):

    """Model Definition house"""
    name = models.CharField(max_length=140)
    price_per_night = models.PositiveIntegerField(verbose_name="Price",help_text="Positive Numbers Only")
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(verbose_name="Pet Allowed?",default=True,help_text="Does this house pet allowed")

    def __str__(self) :
        return self.name

