from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
import requests
import jwt
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import PrivateUserSerializer, TinyUserSerializer
from rest_framework.exceptions import ParseError, NotFound
from .models import User

# Create your views here.

# GET PUT /me private Fields
class Me(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = PrivateUserSerializer(user)
        return Response(serializer.data)

    def put(self, request):
        user = request.user
        serializer = PrivateUserSerializer(
            user,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            user = serializer.save()
            serializer = PrivateUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class Users(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = TinyUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        password = request.data.get("password")
        if not password:
            raise ParseError
        serializer = PrivateUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)
            user.save()
            serializer = PrivateUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class PublicUser(APIView):
    def get(self, request, username):
        try:
            user = User.objects.get(name=username)
        except:
            raise NotFound
        serializer = PrivateUserSerializer(user)
        return Response(serializer.data)


class ChangePassword(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user

        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")
        if not old_password or not new_password:
            raise ParseError
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return Response(status.HTTP_200_OK)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)


class LoginIn(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            raise ParseError
        user = authenticate(
            request,
            username=username,
            password=password,
        )
        if user:
            login(request, user)
            return Response({"ok": "welcom"})
        else:
            return Response({"error": "worng password"})


class LoginOut(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"ok": "bye~"})


class JWTLogin(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            raise ParseError
        user = authenticate(
            request,
            username=username,
            password=password,
        )
        if user:
            token = jwt.encode(
                {"pk": user.pk},
                settings.SECRET_KEY,
                algorithm="HS256",
            )
            return Response({"Token": token})
        else:
            return Response({"error": "worng password"})


class GithubLogin(APIView):
    def post(self, request):
        try:
            code = request.data.get("code")
            access_token = requests.post(
                f"https://github.com/login/oauth/access_token?code={code}&client_id=198ea19e1de6f2a2bdc9&client_secret={settings.GH_SECRET}",
                headers={"Accept": "application/json"},
            )
            access_token = access_token.json().get("access_token")
            user_data = requests.get(
                "https://api.github.com/user",
                headers={
                    "Authorization": f"Bearer {access_token}",
                    "Accept": "application/json",
                },
            )
            user_data = user_data.json()
            user_email = requests.get(
                "https://api.github.com/user/emails",
                headers={
                    "Authorization": f"Bearer {access_token}",
                    "Accept": "application/json",
                },
            )
            user_email = user_data.json()
            try:
                user = User.objects.get(email=user_email[0]["email"])
                login(request, user)
                return Response(status=status.HTTP_200_OK)
            except User.DoesNotExist:
                user = User.objects.create(
                    username=user_data.get("login"),
                    email=user_email[0]["email"],
                    name=user_data.get("name"),
                    avatar=user_data.get("avatar_url"),
                )
                # only login with github
                user.set_unusable_password()
                user.save()
                login(request, user)
                return Response(status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)
