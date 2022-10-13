from django.urls import path
from .views import CategoryViewSet, CategoryDetail

urlpatterns = [
    path(
        "",
        CategoryViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            },
        ),
    ),
    path(
        "<int:pk>",
        CategoryViewSet.as_view(
            {
                "get": "retrieve",
                "put": "partial_update",
                "delete": "destroy",
            },
        ),
    ),
]
