from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class SpecializareSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Specializare
        fields = ["url", "nume"]


class Date_PersonaleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Date_Personale
        fields = ["url", "User", "nume", "sex", "nationalitate", "cetatenie", "data_nasterii",
                  "telefon", "adresa"]


class NoutatiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Noutati
        fields = ["url", "titlu", "anunt", "Date_Personale", "link"]


class MaterieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Materie
        fields = ["url", "nume", "credite"]


class Materiile_GrupelorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Materiile_Grupelor
        fields = ["url", "Materie", "Grupa"]


class Note_Materie_StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note_Materie_Student
        fields = ["url", "Date_Student", "Materiile_Grupelor", "nota"]


class GrupaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Grupa
        fields = ["url", "id_grupa", "Specializare", "an", "grupa", "subgrupa", "link"]


class SemestruSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Semestru
        fields = ["url", "nr_semestru"]


class An_StudiuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = An_Studiu
        fields = ["url", "an"]


class MailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mail
        fields = ["url", "titlu", "emitator", "receptor", "continut"]


class Materiile_ProfesoruluiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Materiile_Profesorului
        fields = ["url", "Date_Profesor", "Materie"]


class Grupa_StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Grupa_Student
        fields = ["url", "Date_Student", "Grupa", ""]