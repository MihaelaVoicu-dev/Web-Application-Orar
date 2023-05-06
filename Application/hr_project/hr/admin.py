from django.contrib import admin
# from .models import Employee, Employer
from .models import *


@admin.register(Grupa)
class GrupaAdmin(admin.ModelAdmin):
    list_display = ["id_specializare", "an", "grupa", "subgrupa"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user

        return queryset


@admin.register(Note_Materie_Student)
class Note_Materie_StudentAdmin(admin.ModelAdmin):
    list_display = ["id_date_personale", "id_materie_grupa"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user

        return queryset


@admin.register(Materiile_Grupelor)
class Materiile_GrupelorAdmin(admin.ModelAdmin):
    list_display = ["id_materie", "id_grupa"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user

        return queryset


@admin.register(Materie)
class MaterieAdmin(admin.ModelAdmin):
    list_display = ["nume", "credite"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user

        return queryset

