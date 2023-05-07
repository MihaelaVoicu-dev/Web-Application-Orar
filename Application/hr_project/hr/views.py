import os

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from rest_framework import viewsets
from rest_framework import permissions
from .serializer import *
from .models import *
from django.shortcuts import render


# def arhiva(request):
#     files = []
#     static_dir = os.path.join(settings.BASE_DIR, 'static/file_backup')
#     for file_name in os.listdir(static_dir):
#         file_path = os.path.join(static_dir, file_name)
#         is_dir = os.path.isdir(file_path)
#         url = f"{settings.STATIC_URL}{file_name}"
#         files.append({'name': file_name, 'is_dir': is_dir, 'url': url})
#     return render(request, 'arhiva.html', {'files': files})


def arhiva(request):
    # Obțineți calea către directorul cu fișiere statice
    static_dir = settings.STATICFILES_DIRS[0]

    # Obțineți lista de fișiere din directorul cu fișiere statice
    files = []
    for root, _, filenames in os.walk(static_dir):
        for filename in filenames:
            files.append(os.path.join(root, filename))
            files[len(files)-1].replace('\\', '/')

    # Încărcați șablonul HTML pentru a afișa lista de fișiere
    template = loader.get_template('arhiva.html')
    context = {'files': files}

    # Răspundeți cu șablonul HTML și lista de fișiere
    return HttpResponse(template.render(context, request))

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to index page.
                return HttpResponseRedirect("http://localhost:8000/date_personale/")
            else:
                # Return a 'disabled account' error message
                return HttpResponse("You're account is disabled.")
    else:
        # the login is a  GET request, so just show the user the login form.
        return render(request, 'sign_in.html')


# def home(request):
#     objects = Grupa_Student.objects.filter(Date_Student__User=request.user.id)
#     objects1 = Grupa.objects.filter()
#     objects2 = Specializare.objects.filter()
#     objects3 = Semestru.objects.filter()
#     context = {'objects': objects, 'objects1': objects1, 'objects2': objects2, 'objects3': objects3}
#     return render(request, 'homepage.html', context)


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