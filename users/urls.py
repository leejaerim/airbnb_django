from django.urls import path
from .views import Me, Users, PublicUser, ChangePassword, LoginIn, LoginOut

urlpatterns = [
    path("", Users.as_view()),
    path("me", Me.as_view()),
    # To not include <me>, django check url from up to down directions.d
    path("@<str:username>", PublicUser.as_view()),
    path("login", LoginIn.as_view()),
    path("logout", LoginOut.as_view()),
    path("change-password", ChangePassword.as_view()),
]
