from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.urls import reverse
from rest_framework import viewsets
from rest_framework import permissions
from .serializer import *
from .models import *
from django.shortcuts import render, redirect
from .forms import *


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to index page.
                return HttpResponseRedirect("http://localhost:8000/send_email/")
            else:
                # Return a 'disabled account' error message
                return HttpResponse("You're account is disabled.")
    else:
        # the login is a  GET request, so just show the user the login form.
        return render(request, 'sign_in.html')
# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None and user.is_active:
#             login(request, user)
#             return redirect("send_email.html")
#         else:
#             error_message = 'Username or password is incorrect.'
#     else:
#         error_message = ''
#     return render(request, 'login.html', {'error_message': error_message})



def send_email(request):

    if request.method == "POST":
        titlu = request.POST.get('titlu')
        receptor = request.POST.get('receptor')
        obj1 = None
        for obj1 in Date_Personale.objects.all():
            if receptor == obj1.adresa_mail:
                break
        emitator = request.user.email
        obj2 = None
        for obj2 in Date_Personale.objects.all():
            if emitator == obj2.User.email:
                emitator = obj2.User.email
                break
        continut = request.POST.get('continut')


        obj = Mail(titlu=titlu, receptor=obj1, emitator=obj2, continut=continut)
        obj.save()
    return render(request, 'send_email.html')


def other_time_table(request):
    objects1 = Specializare.objects.filter()
    objects2 = Grupa.objects.filter()
    context = {'objects1': objects1, 'objects2': objects2}
    return render(request, 'other_time_table.html', context)


def homepage(request):
    # objects = An.objects.filter(an_nume_id =request.user.id)
    # context = {'objects': objects}
    # return render(request, 'homepage.html', context)

    return render(request, 'homepage.html', {
        "name": "DJANGO"
    })


def index(request):
    return render(request, 'index.html', {
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
