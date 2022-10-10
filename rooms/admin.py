from django.contrib import admin
from .models import Room, Amenity

# you must remember 3 parameters
# request parameter is having user information request
@admin.action(description="Set All prices to zero")
def reset_prices(model_admin, request, rooms):
    for room in rooms.all():
        room.price = 0
        room.save()


# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    actions = (reset_prices,)
    list_display = ("name", "price", "kind", "total_amenities", "owner", "rating")

    list_filter = ("price", "amenities")

    def total_amenities(self, room):
        return room.amenities.count()

    search_fields = (
        "^price",  # search keyword startwith
        "=name",  # Exact keyword
        # don't writing acts contains
        "owner__username",
    )


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_filter = ("name", "description", "created_at", "updated_at")
    list_display = ("name", "description", "created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")
