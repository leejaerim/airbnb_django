import strawberry
import typing
from . import types
from .models import Room
from .queries import all_rooms
from rooms import queries
from strawberry.permission import BasePermission
from strawberry.types import Info
from common.permissions import OnlyLoggedIn


@strawberry.type
class Query:
    all_rooms: typing.List[types.Room] = strawberry.field(
        resolver=all_rooms,
        permission_classes=[OnlyLoggedIn],
    )
    # typing.Optional[types.Room] Room type might be nullable.
    room: typing.Optional[types.Room] = strawberry.field(
        resolver=queries.get_room,
    )
