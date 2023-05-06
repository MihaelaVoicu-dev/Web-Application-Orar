from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class MaterieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Materie
        fields = ["url", "nume", "credite"]


class MateriileGrupelorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Materiile_Grupelor
        fields = ["url", "Materie", "Grupa"]


class NoteMaterieStudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note_Materie_Student
        fields = ["url", "Date_Personale", "Materiile_Grupelor"]


class GrupaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Grupa
        fields = ["url", "Specializare", "an", "grupa", "subgrupa"]