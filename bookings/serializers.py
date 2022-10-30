from rest_framework import serializers
from django.utils import timezone
from .models import Booking


class CreateRoomBookingSerializer(serializers.ModelSerializer):
    checkin = serializers.DateField()
    checkout = serializers.DateField()

    class Meta:
        model = Booking
        fields = (
            "checkin",
            "checkout",
            "guests",
        )

    def validate_checkin(self, value):
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("Can't book in past")
        return value

    def validate_checkout(self, value):
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("Can't book in past")
        return value

    def validate(self, data):
        if data["checkout"] <= data["checkin"]:
            raise serializers.ValidationError(
                "Check in Should be smaller then check out."
            )
        if Booking.objects.filter(
            checkin__lte=data["checkout"],
            checkout__gte=data["checkin"],
        ).exists():
            raise serializers.ValidationError("exist booing schedules.")
        return data


class PublicBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = (
            "pk",
            "checkin",
            "checkout",
            "experience_time",
            "guests",
        )
