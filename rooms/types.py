from django.conf import settings
import strawberry
from strawberry.types import Info
import typing
from . import models
from users.types import UserType
from reviews.types import ReviewType
from wishlists.models import Wishlist


@strawberry.django.type(models.Room)
class Room:
    id: strawberry.auto
    name: strawberry.auto
    kind: strawberry.auto
    owner: "UserType"

    @strawberry.field
    def reviews(self, page: typing.Optional[int] = 1) -> typing.List["ReviewType"]:
        page = 1
        page_size = 1
        start = (page - 1) * page_size
        end = start + page_size
        return self.reviews.all()[start:end]

    @strawberry.field
    def rating(self) -> str:
        return self.rating()

    @strawberry.field
    def is_owner(self, info: Info) -> bool:
        # info class has Reqeust info .
        # have to put Info class for injection request data from strawberry
        # type is important to get request data.
        return self.owner == info.context.request.user

    @strawberry.field
    def is_liked(self, info: Info) -> bool:
        return Wishlist.objects.filter(
            user=info.context.request.user,
            rooms__pk=self.pk,
        ).exists()
