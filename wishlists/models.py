from django.db import models
from common.models import CommonModel

# Create your models here.


class Wishlist(CommonModel):
    """wishlist definition"""

    name = models.CharField(max_length=150)
    rooms = models.ManyToManyField(
        "rooms.Room",
        blank=True,
        null=True,
    )
    experiences = models.ManyToManyField(
        "experiences.Experience",
        blank=True,
        null=True,
    )
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
