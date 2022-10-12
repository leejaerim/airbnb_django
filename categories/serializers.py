from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        required=True,
        max_length=50,
    )
    kind = serializers.ChoiceField(
        choices=Category.CategoryKindChoices.choices,
    )
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, valid_data):
        return Category.objects.create(**valid_data)
        # when you  using **, that returns like these.
        # name = '~~', kind = '~~'

    def update(self, instance, valid_data):
        instance.name = valid_data.get("name", instance.name)
        instance.kind = valid_data.get("kind", instance.kind)
        instance.save()
        return instance
