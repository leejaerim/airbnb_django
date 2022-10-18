from django.db import models
from common.models import CommonModel

# Create your models here.
class Room(CommonModel):
    """Room model Definition"""

    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVATE_ROOM = ("private_room", "Private Room")
        SHARED_ROOM = ("shared_room", "Shared Room")

    name = models.CharField(max_length=180, default="TEST")
    country = models.CharField(max_length=50, default="한국")
    city = models.CharField(max_length=80, default="서울")
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=250)
    pet_frendly = models.BooleanField(default=True)
    kind = models.CharField(
        max_length=20,
        choices=RoomKindChoices.choices,
    )
    # many to many Field
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="rooms",
    )
    amenities = models.ManyToManyField(
        "rooms.Amenity",
        related_name="rooms",
    )
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="rooms",
    )

    def __str__(self):
        return self.name

    def rating(room):
        reviews = room.reviews.all()
        if len(reviews) == 0:
            return 0
        else:
            total_rating = 0
            # for i in reviews:
            #    total_rating += i.rating
            # Optimize Query
            for i in reviews.values("rating"):
                total_rating += i["rating"]
            return round(total_rating / reviews.count(), 2)


class Amenity(CommonModel):
    """Amenity Definition"""

    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "amenities"
