from django.db import models
from common.models import CommonModel

# Create your models here.
class Experience(CommonModel):
    name = models.CharField(max_length=250, default="")
    country = models.CharField(max_length=50, default="한국")
    city = models.CharField(max_length=80, default="서울")
    host = models.ForeignKey("users.User", on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=250)
    start = models.TimeField()
    end = models.TimeField()
    description = models.TextField()
    perks = models.ManyToManyField(
        "experiences.Perk",
        related_name="experiences",
    )
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="experiences",
    )

    def __str__(self):
        return self.name


class Perk(CommonModel):
    """what is included on an Experience"""

    name = models.CharField(
        max_length=100,
    )
    details = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Perks"
