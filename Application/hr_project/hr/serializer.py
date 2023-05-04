from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Materie, An, Grupa, Profesor, Orar, Sala, Zi


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class MaterieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Materie
        fields = ["url", "nume_materie"]

    def get_fields(self):
        fields = super().get_fields()  # Python 3 syntax
        request = self.context.get("request", None)
        if request and request.user and request.user.is_superuser is False:
            fields["nume_materie"].read_only = True
        return fields


class AnSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = An
        fields = ["url", "id_an"]

    def get_fields(self):
        fields = super().get_fields()  # Python 3 syntax
        request = self.context.get("request", None)
        if request and request.user and request.user.is_superuser is False and request.user.is_staff is True:
            fields["id_an"].read_only = True
        return fields


class GrupaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Grupa
        fields = ["url", "id_grupa", "an", "grupa"]

    def get_fields(self):
        fields = super().get_fields()  # Python 3 syntax
        request = self.context.get("request", None)
        if request and request.user and request.user.is_superuser is False:
            fields["id_grupa"].read_only = True
            fields["an"].read_only = True
            fields["grupa"].read_only = True
        return fields


class SalaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sala
        fields = ["url", "id_sala", "nume_sala"]

    def get_fields(self):
        fields = super().get_fields()  # Python 3 syntax
        request = self.context.get("request", None)
        if request and request.user and request.user.is_superuser is False:
            fields["id_sala"].read_only = True
            fields["nume_sala"].read_only = True
        return fields


class ProfesorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profesor
        fields = ["url", "CNP", "nume_profesor", "prenume_profesor"]

    def get_fields(self):
        fields = super().get_fields()  # Python 3 syntax
        request = self.context.get("request", None)
        if request and request.user and request.user.is_superuser is False:
            fields["CNP"].read_only = True
            fields["nume_profesor"].read_only = True
            fields["prenume_profesor"].read_only = True
        return fields


class ZiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Zi
        fields = ["url", "nume_zi"]

    def get_fields(self):
        fields = super().get_fields()  # Python 3 syntax
        request = self.context.get("request", None)
        if request and request.user and request.user.is_superuser is False:
            fields["nume_zi"].read_only = True
        return fields


class OrarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Orar
        fields = ["url", "an", "grupa", "zi", "materie", "profesor", "sala", "inceput_ora", "sfarsit_ora"]

    def get_fields(self):
        fields = super().get_fields()  # Python 3 syntax
        request = self.context.get("request", None)
        if request and request.user and request.user.is_superuser is True:
            pass
        else:
            fields["an"].read_only = True
            fields["grupa"].read_only = True
            fields["zi"].read_only = True
            fields["materie"].read_only = True
            fields["profesor"].read_only = True
            fields["sala"].read_only = True
            fields["inceput_ora"].read_only = True
            fields["sfarsit_ora"].read_only = True
        return fields
