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
        verbose_name_plural = 'An Studiu'

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

    id_specializare.short_description = "Specializare"
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

    link = models.CharField(
        max_length=200,
        null=False
    )


class Date_Personale(models.Model):
    class Meta:
        db_table = 'date_personale'
        verbose_name_plural = 'Date Personale'

    def __str__(self):
        return self.User.email

    User = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def cnp(self):
        return self.User.username

    cnp.short_description = "CNP"
    cnp.admin_order_field = "User__username"

    def adresa_mail(self):
        return self.User.email

    adresa_mail.short_description = "Adresa Mail"
    adresa_mail.admin_order_field = "User__adresa_mail"

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


class Mail(MyModel):
    class Meta:
        db_table = 'mail'
        verbose_name_plural = 'Mail'

    def __str__(self):
        return self.titlu

    titlu = models.CharField(
        max_length=50,
        null=False
    )
    receptor = models.ForeignKey(Date_Personale, on_delete=models.CASCADE, related_name="receptor")
    emitator = models.ForeignKey(Date_Personale, on_delete=models.CASCADE, related_name="emitator")

    def r_adresa_mail(self):
        return self.receptor.User.email

    r_adresa_mail.short_description = "Receptor"
    r_adresa_mail.admin_order_field = "receptor__adresa_mail"

    def e_adresa_mail(self):
        return self.emitator.User.email

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
        return f'{self.Materie} {self.Date_Profesor}'

    Materie = models.ForeignKey(Materie, on_delete=models.CASCADE)

    def m_materie(self):
        return self.Materie.nume

    m_materie.short_description = "Materie"
    m_materie.admin_order_field = "materie__nume"

    Date_Profesor = models.ForeignKey(Date_Personale, on_delete=models.CASCADE,
                                      limit_choices_to={'User__is_active': True, 'User__is_staff': True,
                                                        'User__is_superuser': False})

    def email_profesor(self):
        return self.Date_Profesor.User.email

    email_profesor.short_description = "Adresa Profesor"
    email_profesor.admin_order_field = "Date_Profesor__adresa_mail"


class Noutati(models.Model):
    class Meta:
        db_table = 'noutati'
        verbose_name_plural = 'Noutati'

    def __str__(self):
        return self.titlu

    titlu = models.CharField(
        max_length=50,
        null=False
    )

    anunt = models.CharField(
        max_length=200,
        null=False
    )

    link = models.CharField(
        max_length=200,
        null=False
    )

    Date_Personale = models.ForeignKey(Date_Personale, on_delete=models.CASCADE)

    def adresa_mail(self):
        return self.Date_Personale.User.email

    adresa_mail.short_description = "Adresa Mail"
    adresa_mail.admin_order_field = "Date_Personale__adresa_mail"


class Materiile_Grupelor(MyModel):
    class Meta:
        db_table = 'materiile_grupelor'
        verbose_name_plural = 'Materiile Grupelor'

    def __str__(self):
        return f'{self.Grupa.id_grupa} {self.Materie.nume}'

    ID_mat_grupa = models.DecimalField(
        decimal_places=0,
        max_digits=100,
        null=False
    )

    Grupa = models.ForeignKey(Grupa, on_delete=models.CASCADE)

    def id_grupa(self):
        return self.Grupa.grupa

    id_grupa.short_description = "Grupa"
    id_grupa.admin_order_field = "Grupa__id_grupa"

    Materie = models.ForeignKey(Materie, on_delete=models.CASCADE)

    def id_materie(self):
        return self.Materie.nume

    id_materie.short_description = "Materie"
    id_materie.admin_order_field = "Materie__nume"


class Note_Materie_Student(MyModel):
    class Meta:
        db_table = 'note_materie_student'
        verbose_name_plural = 'Note Materii Student'

    def __str__(self):
        return str(self.nota)

    Date_Student = models.ForeignKey(Date_Personale, on_delete=models.CASCADE,
                                       limit_choices_to={'User__is_active': True, 'User__is_staff': False,
                                                         'User__is_superuser': False})

    def email_student(self):
        return str(self.Date_Student.nume)

    email_student.short_description = "Email Student"
    email_student.admin_order_field = "Date_Student__nume"

    Materiile_Grupelor = models.ForeignKey(Materiile_Grupelor, on_delete=models.CASCADE)

    def id_materie_grupa(self):
        return str(self.Materiile_Grupelor.ID_mat_grupa)

    id_materie_grupa.short_description = "ID Materie Grupa"
    id_materie_grupa.admin_order_field = "Id_materie_grupa__ID_mat_grupa"

    nota = models.DecimalField(
        null=False,
        decimal_places=0,
        max_digits=100
    )


class Grupa_Student(MyModel):
    class Meta:
        db_table = 'grupa_student'
        verbose_name_plural = 'Grupele Studentilor'

    def __str__(self):
        return f'{self.Date_Student} {self.Grupa}'

    An_Studiu = models.ForeignKey(An_Studiu, on_delete=models.CASCADE)

    def id_an_studiu(self):
        return self.An_Studiu.an

    id_an_studiu.short_description = "Anul De Studiu"
    id_an_studiu.admin_order_field = "An_Studiu__id_an"

    Grupa = models.ForeignKey(Grupa, on_delete=models.CASCADE)

    def id_grupa(self):
        return self.Grupa.id_grupa

    id_grupa.short_description = "Grupa"
    id_grupa.admin_order_field = "Grupa__id_grupa"

    Date_Student = models.ForeignKey(Date_Personale, on_delete=models.CASCADE,
                                     limit_choices_to={'User__is_active': True, 'User__is_staff': False,
                                                       'User__is_superuser': False})

    def email_student(self):
        return self.Date_Student.User.email

    email_student.short_description = "Email Student"
    email_student.admin_order_field = "Date_Student__adresa_mail"

    link = models.CharField(
        max_length=200,
        null=False
    )