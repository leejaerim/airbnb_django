from .models import Room


def all_rooms():
    return Room.objects.all()
