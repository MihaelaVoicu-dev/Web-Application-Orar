from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class SpecializareSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "nume"]


class Date_PersonaleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "cnp", "nume", "sex", "nationalitate", "cetatenie", "telefon", "adresa", "adresa_mail", "semestru", "an_studiu"]


class NoutatiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "titlu", "anunt", "adresa_mail"]


