from dataclasses import field
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Amenity, Room
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer
from reviews.serializers import ReviewSerializer
from medias.serializers import PhotoSerializer
from wishlists.models import Wishlist


class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = ("id", "name", "description")


class RoomDetailSerializer(ModelSerializer):
    owner = TinyUserSerializer(read_only=True)
    amenities = AmenitySerializer(
        read_only=True, many=True
    )  # when using List , many =True
    category = CategorySerializer(
        read_only=True,
    )
    rating = SerializerMethodField()
    is_liked = SerializerMethodField()
    is_owner = SerializerMethodField()
    reviews = ReviewSerializer(
        many=True,
        read_only=True,
    )
    photos = PhotoSerializer(
        many=True,
        read_only=True,
    )

    def get_is_owner(self, room):
        request = self.context["request"]
        return room.owner == request.user

    class Meta:
        model = Room
        fields = "__all__"

    def get_rating(self, room):
        return room.rating()

    def create(self, valid_data):
        return  # Room.objects.create(**valid_data)

    def get_is_liked(self, room):
        request = self.context["request"]
        # 유저가 존재하는지 여부
        if request.user.is_authenticated:
            # 유저가 만든 wishlist 중에서 room pk 체크
            return Wishlist.objects.filter(
                user=request.user, rooms__id=room.pk
            ).exists()
        return False


class RoomListSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = (
            "pk",
            "name",
            "country",
            "city",
            "price",
            "rating",
            "is_owner",
            "photos",
        )

    is_owner = SerializerMethodField()
    photos = PhotoSerializer(
        many=True,
        read_only=True,
    )

    def get_is_owner(self, room):
        request = self.context["request"]
        return room.owner == request.user

    rating = SerializerMethodField()

    def get_rating(self, room):
        return room.rating()
