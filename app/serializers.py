# -*- coding: utf-8 -*-
from custom_user.models import EmailUser
from rest_framework import serializers, viewsets

__author__ = "MDee"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailUser


class UserViewSet(viewsets.ModelViewSet):
    model = EmailUser
    serializer_class = UserSerializer