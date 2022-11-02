from .models import Room


def all_rooms():
    # if info.context.request.user.is_authenticated:
    return Room.objects.all()

    # else:
    #    raise Exception("Not Auth.")


def get_room(pk: int):
    try:
        return Room.objects.get(pk=pk)
    except:
        return None
