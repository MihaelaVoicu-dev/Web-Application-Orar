from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


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
        fields = ["url", "titlu","emitator","receptor","continut"]

class Materiile_ProfesoruluiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Materiile_Profesorului
        fields = ["url", "materie","CNP_profesor"]


