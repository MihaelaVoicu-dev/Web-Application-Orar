from django.db import models
from django.conf import settings


class MyModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class An_Studiu(MyModel):
    class Meta:
        db_table = 'an_studiu'
        verbose_name_plural = 'ani_studiu'

    def __str__(self):
        return str(self.an)

    an = models.DecimalField(
        max_digits=2,
        decimal_places=0,
        default=0,
        null=False
    )


class Specializare(MyModel):
    class Meta:
        db_table = 'specializare'
        verbose_name_plural = 'Specializari'

    def __str__(self):
        return self.nume

    nume = models.CharField(
        max_length=50,
        null=False
    )


class Semestru(MyModel):
    class Meta:
        db_table = 'semestru'
        verbose_name_plural = 'semestre'

    def __str__(self):
        return str(self.nr_semestru)

    nr_semestru = models.DecimalField(
        max_digits=2,
        decimal_places=0,
        default=0,
        null=False
    )
class Grupa(MyModel):
    class Meta:
        db_table = 'grupa'
        verbose_name_plural = 'Grupe'

    def __str__(self):
        return self.id_grupa

    Specializare = models.ForeignKey(Specializare, on_delete=models.CASCADE)

    def id_specializare(self):
        return self.Specializare.nume

    id_specializare.short_description = "ID_Specializare"
    id_specializare.admin_order_field = "Specializare__id_specializare"

    id_grupa = models.CharField(
        max_length=50,
        null=False
    )

    an = models.DecimalField(
        null=False,
        max_digits=100,
        decimal_places=0
    )

    grupa = models.CharField(
        max_length=50,
        null=False
    )

    subgrupa = models.CharField(
        max_length=50,
        null=False
    )



class Date_Personale(models.Model):
    class Meta:
        db_table = 'date_personale'
        verbose_name_plural = 'Date_Personale'

    def __str__(self):
        return self.CNP.username

    CNP = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def cnp_s(self):
        return self.CNP.username

    cnp_s.short_description = "CNP"
    cnp_s.admin_order_field = "CNP__username"

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
        max_length=200,
        null=False
    )

    adresa_mail = models.CharField(
        max_length=50,
        null=False
    )

    grupa = models.ForeignKey(Grupa, on_delete=models.CASCADE)
    semestru = models.ForeignKey(Semestru, on_delete=models.CASCADE)
    an_studiu = models.ForeignKey(An_Studiu, on_delete=models.CASCADE)

    def id_grupa(self):
        return self.grupa.id_grupa

    id_grupa.short_description = "Grupa"
    id_grupa.admin_order_field = "grupa__id_grupa"
    def id_an_studiu(self):
        return self.an_studiu.an

    id_an_studiu.short_description = "Anul De Studiu"
    id_an_studiu.admin_order_field = "an__id_an"

    def id_semestru(self):
        return self.semestru.nr_semestru

    id_semestru.short_description = "Semestru"
    id_semestru.admin_order_field = "semestru__nr_semestru"


class Mail(MyModel):
    class Meta:
        db_table = 'mail'
        verbose_name_plural = 'mailuri'

    def __str__(self):
        return self.titlu

    titlu = models.CharField(
        max_length=50,
        null=False
    )
    receptor = models.ForeignKey(Date_Personale, on_delete=models.CASCADE, related_name="receptor")
    emitator = models.ForeignKey(Date_Personale, on_delete=models.CASCADE, related_name="emitator")

    def r_adresa_mail(self):
        return self.receptor.adresa_mail

    r_adresa_mail.short_description = "Receptor"
    r_adresa_mail.admin_order_field = "receptor__adresa_mail"

    def e_adresa_mail(self):
        return self.emitator.adresa_mail

    e_adresa_mail.short_description = "Emitator"
    e_adresa_mail.admin_order_field = "emitator__adresa_mail"
    continut = models.CharField(
        max_length=200,
        null=False
    )


class Materie(MyModel):
    class Meta:
        db_table = 'materie'
        verbose_name_plural = 'Materii'

    def __str__(self):
        return self.nume

    nume = models.CharField(
        max_length=50,
        null=False
    )

    credite = models.DecimalField(
        null=False,
        decimal_places=0,
        max_digits=100
    )


class Materiile_Profesorului(MyModel):
    class Meta:
        db_table = 'materiile_profesorului'
        verbose_name_plural = 'Materiile Profesorului'

    def __str__(self):
        return f'{self.materie} {self.CNP_profesor}'
    titlu = models.CharField(
        max_length=50,
        null=False
    )
    materie = models.ForeignKey(Materie, on_delete=models.CASCADE)
    CNP_profesor = models.ForeignKey(Date_Personale, on_delete=models.CASCADE)

    def m_materie(self):
        return self.materie.nume

    m_materie.short_description = "Materie"
    m_materie.admin_order_field = "materie__nume"

    def cnp_profesor(self):
        return self.CNP_profesor.CNP.username

    cnp_profesor.short_description = "CNP Profesor"
    cnp_profesor.admin_order_field = "CNP_Profesor__cnp_s"


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
        max_length=200,
        null=False
    )

    def id_adresa_mail(self):
        return self.adresa_mail.adresa_mail

    id_adresa_mail.short_description = "Anul De Studiu"
    id_adresa_mail.admin_order_field = "an__id_an"


class Materiile_Grupelor(MyModel):
    class Meta:
        db_table = 'materiile_grupelor'
        verbose_name_plural = 'materiile_grupelor'

    def __str__(self):
        return f'{self.Grupa.id_grupa} {self.Materie.nume}'

    Materie = models.ForeignKey(Materie, on_delete=models.CASCADE)
    Grupa = models.ForeignKey(Grupa, on_delete=models.CASCADE)

    ID_mat_grupa = models.DecimalField(
        decimal_places=0,
        max_digits=100,
        null=False
    )

    def id_grupa(self):
        return self.Grupa.grupa

    id_grupa.short_description = "ID_Grupa"
    id_grupa.admin_order_field = "Grupa__id_grupa"

    def id_materie(self):
        return self.Materie.nume

    id_materie.short_description = "ID_Materie"
    id_materie.admin_order_field = "Materie__nume"


class Note_Materie_Student(MyModel):
    class Meta:
        db_table = 'note_materie_student'
        verbose_name_plural = 'Note_materii_student'

    def __str__(self):
        return str(self.nota)

    Date_Personale = models.ForeignKey(Date_Personale, on_delete=models.CASCADE)
    Materiile_Grupelor = models.ForeignKey(Materiile_Grupelor, on_delete=models.CASCADE)

    def id_date_personale(self):
        return str(self.Date_Personale.CNP.username)

    id_date_personale.short_description = "ID_Date_Personale"
    id_date_personale.admin_order_field = "Id_date_personale__cnp"

    def id_materie_grupa(self):
        return str(self.Materiile_Grupelor.ID_mat_grupa)

    id_materie_grupa.short_description = "ID_mat_grupa"
    id_materie_grupa.admin_order_field = "Id_materie_grupa__ID_mat_grupa"

    nota = models.DecimalField(
        null=False,
        decimal_places=0,
        max_digits=100
    )
