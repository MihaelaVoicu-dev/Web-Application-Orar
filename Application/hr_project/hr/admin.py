from django.contrib import admin
# from .models import Employee, Employer
from .models import *


@admin.register(Date_Personale)
class Date_PersonaleAdmin(admin.ModelAdmin):
    list_display = ["nume", "cnp", "sex", "nationalitate", "cetatenie", "telefon", "adresa", "adresa_mail", "id_semestru", "id_an_studiu"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user

        return queryset


@admin.register(Specializare)
class SpecializareAdmin(admin.ModelAdmin):
    list_display = ["nume"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user

        return queryset


@admin.register(Noutati)
class NoutatiAdmin(admin.ModelAdmin):
    list_display = ["titlu", "anunt", "id_adresa_mail"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user

        return queryset



