from rest_framework import viewsets
from rest_framework import permissions
from .serializer import *
from .models import *
from static import *
from django.shortcuts import render


def homepage(request):
    # objects = An.objects.filter(an_nume_id =request.user.id)
    #context = {'objects': objects}
    #return render(request, 'homepage.html', context)
     return render(request, 'homepage.html', {
         "name": "DJANGO"
     })


def index(request):
    return render(request, 'index.html',{
        "name": "DJANGO"
    })
def casutaPostala(request):
    objects = Mail.objects.filter(receptor__CNP = request.user.id)
    context = {'objects': objects}
    return render(request, 'mailbox/index.html', context)
def situatieScolara(request):
    objects = Date_Personale.objects.filter(CNP=request.user.id)
    objects1 = Grupa.objects.filter()
    objects2 = Specializare.objects.filter()
    objects3 = Semestru.objects.filter()
    context = {'objects': objects, 'objects1': objects1, 'objects2': objects2, 'objects3': objects3}
    return render(request, 'situatieScolara/index.html', context)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAuthenticated]


class MaterieViewSet(viewsets.ModelViewSet):
    queryset = Materie.objects.all()
    serializer_class = MaterieSerializer
    permission_classes = [permissions.IsAuthenticated]


class Materiile_GrupelorViewSet(viewsets.ModelViewSet):
    queryset = Materiile_Grupelor.objects.all()
    serializer_class = Materiile_GrupelorSerializer
    permission_classes = [permissions.IsAuthenticated]


class GrupaViewSet(viewsets.ModelViewSet):
    queryset = Grupa.objects.all()
    serializer_class = GrupaSerializer
    permission_classes = [permissions.IsAuthenticated]


class Note_Materie_StudentViewSet(viewsets.ModelViewSet):
    queryset = Note_Materie_Student.objects.all()
    serializer_class = Note_Materie_StudentSerializer
    permission_classes = [permissions.IsAuthenticated]


class Date_PersonaleViewSet(viewsets.ModelViewSet):
    queryset = Date_Personale.objects.all()
    serializer_class = Date_PersonaleSerializer
    permission_classes = [permissions.IsAuthenticated]


class NoutatiViewSet(viewsets.ModelViewSet):
    queryset = Noutati.objects.all()
    serializer_class = NoutatiSerializer
    permission_classes = [permissions.IsAuthenticated]


class SpecializareViewSet(viewsets.ModelViewSet):
    queryset = Specializare.objects.all()
    serializer_class = SpecializareSerializer
    permission_classes = [permissions.IsAuthenticated]


class SemestruViewSet(viewsets.ModelViewSet):
    queryset = Semestru.objects.all()
    serializer_class = SemestruSerializer
    permission_classes = [permissions.IsAuthenticated]


class An_StudiuViewSet(viewsets.ModelViewSet):
    queryset = An_Studiu.objects.all()
    serializer_class = An_StudiuSerializer
    permission_classes = [permissions.IsAuthenticated]


class Materiile_ProfesoruluiViewSet(viewsets.ModelViewSet):
    queryset = Materiile_Profesorului.objects.all()
    serializer_class = Materiile_ProfesoruluiSerializer
    permission_classes = [permissions.IsAuthenticated]


class MailViewSet(viewsets.ModelViewSet):
    queryset = Mail.objects.all()
    serializer_class = MailSerializer
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = Note_Materie_StudentSerializer
    permission_classes = [permissions.IsAuthenticated]