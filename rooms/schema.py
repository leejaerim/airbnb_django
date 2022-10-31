import strawberry
import typing
from . import types
from .models import Room
from .queries import all_rooms


@strawberry.type
class Query:
    all_rooms: typing.List[types.Room] = strawberry.field(resolver=all_rooms)
