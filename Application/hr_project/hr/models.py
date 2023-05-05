from django.db import models
from django.conf import settings


class MyModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Date_Personale(models.Model):
    class Meta:
        db_table = 'date_personale'
        verbose_name_plural = 'Date_Personale'

    def __str__(self):
        return self.cnp

    semestru = models.ForeignKey(Semestru, on_delete=models.CASCADE)
    an_studiu = models.ForeignKey(An_Studiu, on_delete=models.CASCADE)

    cnp = models.CharField(
        max_length=13,
        null=False
    )

    nume = models.CharField(
        max_length=50,
        null=False
    )

    sex = models.CharField(
        max_length=1,
        null=False
    )

    nationalitate = models.CharField(
        max_length=50,
        null=False
    )

    cetatenie = models.CharField(
        max_length=50,
        null=False
    )

    data_nasterii = models.DateTimeField(
        auto_now_add=True
    )

    telefon = models.CharField(
        max_length=10,
        null=False
    )

    adresa = models.CharField(
        null=False
    )

    adresa_mail = models.CharField(
        null=False
    )

    def id_an_studiu(self):
        return self.an_studiu.an

    id_an_studiu.short_description = "Anul De Studiu"
    id_an_studiu.admin_order_field = "an__id_an"

    def id_semestru(self):
        return self.semestru.nr_semestru

    id_semestru.short_description = "Semestru"
    id_semestru.admin_order_field = "semestru__nr_semestru"


class Specializare(MyModel):
    class Meta:
        db_table = 'specializare'
        verbose_name_plural = 'Specializari'

    def str(self):
        return self.nume

    nume = models.CharField(
            max_length=50,
            null=False
    )


class Noutati(models.Model):
    class Meta:
        db_table = 'noutati'
        verbose_name_plural = 'Noutati'

    def __str__(self):
        return self.titlu

    adresa_mail = models.ForeignKey(Date_Personale, on_delete=models.CASCADE)

    titlu = models.CharField(
        max_length=50,
        null=False
    )

    anunt = models.CharField(
        null=False
    )

    def id_adresa_mail(self):
        return self.adresa_mail.adresa_mail

    id_adresa_mail.short_description = "Anul De Studiu"
    id_adresa_mail.admin_order_field = "an__id_an"


# class Materie(MyModel):
#     class Meta:
#         db_table = 'materie'
#         verbose_name_plural = 'Materii'
#
#     def __str__(self):
#         return self.nume_materie
#
#     nume_materie = models.CharField(
#         max_length=50,
#         null=False
#     )
#
#
# class Grupa(MyModel):
#     class Meta:
#         db_table = 'grupa'
#         verbose_name_plural = 'Grupe'
#
#     def __str__(self):
#         return f'{self.an}.{self.grupa}'
#
#     an = models.DecimalField(
#         max_digits=2,
#         decimal_places=0,
#         default=0,
#         null=False
#     )
#     grupa = models.CharField(
#         max_length=5,
#         null=False
#     )
#
#
# class An(MyModel):
#     class Meta:
#         db_table = 'an'
#         verbose_name_plural = 'Ani'
#
#     def __str__(self):
#         return self.id_an
#
#     id_an = models.CharField(
#         max_length=9,
#         null=False
#     )
#
#     an_nume = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE
#     )
#
#
# class Zi(MyModel):
#     class Meta:
#         db_table = 'zi'
#         verbose_name_plural = 'Zile'
#
#     def __str__(self):
#         return self.nume_zi
#
#     nume_zi = models.CharField(
#         max_length=8,
#         null=False
#     )
#
#
# class Sala(MyModel):
#     class Meta:
#         db_table = 'sala'
#         verbose_name_plural = 'Sali'
#
#     def __str__(self):
#         return self.id_sala
#
#     id_sala = models.CharField(
#         max_length=10,
#         null=False
#     )
#
#     nume_sala = models.CharField(
#         max_length=30,
#         null=False
#     )
#
#
# class Profesor(MyModel):
#     class Meta:
#         db_table = 'profesor'
#         verbose_name_plural = 'Profesori'
#
#     def __str__(self):
#         return f'{self.nume_profesor} {self.prenume_profesor}'
#
#     CNP = models.CharField(
#         max_length=13,
#         null=False
#     )
#     nume_profesor = models.CharField(
#         max_length=15,
#         null=False
#     )
#     prenume_profesor = models.CharField(
#         max_length=15,
#         null=False
#     )
#
#
# class Orar(MyModel):
#     class Meta:
#         db_table = 'orar'
#         verbose_name_plural = 'Orare'
#
#     an = models.ForeignKey(An, on_delete=models.CASCADE)
#     grupa = models.ForeignKey(Grupa, on_delete=models.CASCADE)
#     zi = models.ForeignKey(Zi, on_delete=models.CASCADE)
#     materie = models.ForeignKey(Materie, on_delete=models.CASCADE)
#     profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
#     sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
#     inceput_ora = models.TimeField(auto_now=False, auto_now_add=False)
#     sfarsit_ora = models.TimeField(auto_now=False, auto_now_add=False)
#
#     def id_an(self):
#         return self.an.id_an
#
#     id_an.short_description = "Anul"
#     id_an.admin_order_field = "an__id_an"
#
#     def g_an(self):
#         return self.grupa.an
#
#     g_an.short_description = "An"
#     g_an.admin_order_field = "grupa__an"
#
#     def g_grupa(self):
#         return self.grupa.grupa
#
#     g_grupa.short_description = "Grupa"
#     g_grupa.admin_order_field = "grupa__grupa"
#
#     def nume_zi(self):
#         return self.zi.nume_zi
#
#     nume_zi.short_description = "Ziua"
#     nume_zi.admin_order_field = "zi__nume_zi"
#
#     def nume_materie(self):
#         return self.materie.nume_materie
#
#     nume_materie.short_description = "Materie"
#     nume_materie.admin_order_field = "materie__nume_materie"
#
#     def nume_profesor(self):
#         return self.profesor.nume_profesor
#
#     nume_profesor.short_description = "Nume Profesor"
#     nume_profesor.admin_order_field = "profesor__nume_profesor"
#
#     def prenume_profesor(self):
#         return self.profesor.prenume_profesor
#
#     prenume_profesor.short_description = "Prenume Profesor"
#     prenume_profesor.admin_order_field = "profesor__prenume_profesor"
#
#     def id_sala(self):
#         return self.sala.id_sala
#
#     id_sala.short_description = "Sala"
#     id_sala.admin_order_field = "sala__id_sala"
