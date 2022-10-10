from django.contrib import admin
from .models import Review


class WordFilter(admin.SimpleListFilter):
    title = "Filter by words!"
    parameter_name = "word"

    def lookups(self, request: any, model_admin: any) -> list[tuple[any, str]]:
        return [
            (
                "good",
                "Good",
            ),
            (
                "great",
                "Great",
            ),
        ]

    def queryset(self, request, reviews):
        word = self.value()
        if not word:
            return reviews
        return reviews.filter(payload__contains=word)


# Register your models here.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("__str__", "payload")
    list_filter = (
        WordFilter,
        "rating",
        "user__username",
        "room__category",
    )
