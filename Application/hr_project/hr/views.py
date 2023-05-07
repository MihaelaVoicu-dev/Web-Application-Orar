from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import permissions
from .serializer import *
from .models import *
from django.shortcuts import render

# def arhiva(request):
#     return render(request, 'arhiva.html', {
#         "name": "DJANGO"
#     })


def home(request):
    objects = Grupa_Student.objects.filter(Date_Student__User=request.user.id)
    objects1 = Grupa.objects.filter()
    objects2 = Specializare.objects.filter()
    objects3 = Semestru.objects.filter()
    context = {'objects': objects, 'objects1': objects1, 'objects2': objects2, 'objects3': objects3}
    return render(request, 'homepage.html', context)

def date_personale(request):
    date = Date_Personale.objects.filter(User=request.user.id).first()
    context = {'date': date}
    return render(request, 'date_personale.html', context)


def pagina_principala(request):
    # objects = An.objects.filter(an_nume_id =request.user.id)
    # context = {'objects': objects}
    # return render(request, 'homepage.html', context)
    noutati = Noutati.objects.order_by('-id')[:3]
    context = {
        'noutate1': noutati[0],
        'noutate2': noutati[1],
        'noutate3': noutati[2]
    }
    return render(request, 'pagina_principala.html', context)
    # return render(request, 'pagina_principala.html', {
    #     "name": "DJANGO"
    # })



def index(request):
    return render(request, 'pagina_principala.html',{
        "name": "DJANGO"
    })


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


class Grupa_StudentViewSet(viewsets.ModelViewSet):
    queryset = Grupa_Student.objects.all()
    serializer_class = Grupa_StudentSerializer
    permission_classes = [permissions.IsAuthenticated]