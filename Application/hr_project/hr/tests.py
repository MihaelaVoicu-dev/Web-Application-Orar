from django.test import TestCase
from .models import *
from django.contrib.auth.models import User


class MaterieTestCase(TestCase):
    def setUp(self):
        # Create a Materie object for testing
        self.materie = Materie.objects.create(
            nume='Test Materie',
            credite=6
        )

    def test_materie_creation(self):
        # Verify if the Materie object was created successfully
        test_materie = Materie.objects.get(nume='Test Materie')
        self.assertEqual(test_materie.nume, 'Test Materie')
        self.assertEqual(test_materie.credite, 6)

    def test_materie_update(self):
        # Update the Materie object for the test
        test_materie = Materie.objects.get(nume='Test Materie')
        test_materie.credite = 10
        test_materie.save()

        # Verify if the Materie object was updated successfully
        updated_materie = Materie.objects.get(nume='Test Materie')
        self.assertEqual(updated_materie.credite, 10)

    def test_materie_deletion(self):
        # Delete the Materie object for the test
        test_materie = Materie.objects.get(nume='Test Materie')
        test_materie.delete()

        # Verify if the Materie object was deleted successfully
        with self.assertRaises(Materie.DoesNotExist):
            Materie.objects.get(nume='Test Materie')


class DatePersonaleTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='12345'
        )
        self.date_personale = Date_Personale.objects.create(
            User=self.user,
            nume='Doe',
            sex='M',
            nationalitate='romana',
            cetatenie='romana',
            telefon='0123456789',
            adresa='Bucuresti, Romania'
        )

    def test_date_personale_creation(self):
        test_date_personale = Date_Personale.objects.get(User=self.user)
        self.assertEqual(test_date_personale.nume, 'Doe')

    def test_date_personale_update(self):
        test_date_personale = Date_Personale.objects.get(User=self.user)
        test_date_personale.nume = 'John Doe'
        test_date_personale.save()
        self.assertEqual(test_date_personale.nume, 'John Doe')

    def test_date_personale_deletion(self):
        test_date_personale = Date_Personale.objects.get(User=self.user)
        test_date_personale.delete()
        self.assertRaises(
            Date_Personale.DoesNotExist,
            Date_Personale.objects.get,
            User=self.user
        )


class NoutatiTestCase(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )

        # Create a Date_Personale object associated with the user
        self.date_personale = Date_Personale.objects.create(
            User=self.user,
            nume='Test User',
            sex='M',
            nationalitate='Romanian',
            cetatenie='Romanian',
            telefon='1234567890',
            adresa='Test Address'
        )

        # Create a Noutati object associated with the Date_Personale object
        self.noutati = Noutati.objects.create(
            titlu='Test Title',
            anunt='Test Announcement',
            link='https://example.com',
            Date_Personale=self.date_personale
        )

    def test_noutati_creation(self):
        # Verify that the Noutati object was created successfully in the database
        test_noutati = Noutati.objects.get(titlu='Test Title')
        self.assertEqual(test_noutati.titlu, 'Test Title')
        self.assertEqual(test_noutati.anunt, 'Test Announcement')
        self.assertEqual(test_noutati.link, 'https://example.com')
        self.assertEqual(test_noutati.Date_Personale, self.date_personale)

    def test_noutati_update(self):
        # Update the Noutati object's title and save it to the database
        test_noutati = Noutati.objects.get(titlu='Test Title')
        test_noutati.titlu = 'New Test Title'
        test_noutati.save()

        # Verify that the changes were saved successfully in the database
        updated_noutati = Noutati.objects.get(titlu='New Test Title')
        self.assertEqual(updated_noutati.titlu, 'New Test Title')

    def test_noutati_deletion(self):
        # Delete the Noutati object and verify that it no longer exists in the database
        test_noutati = Noutati.objects.get(titlu='Test Title')
        test_noutati.delete()
        self.assertRaises(Noutati.DoesNotExist, Noutati.objects.get, titlu='Test Title')


class An_StudiuTestCase(TestCase):
    def setUp(self):
        An_Studiu.objects.create(an=5)

    def test_an_studiu_creation(self):
        # Verificăm dacă obiectul de tip Grupa a fost creat cu succes în baza de date
        test_an_studiu = An_Studiu.objects.get(an=5)
        self.assertEqual(test_an_studiu.an, 5)

    def test_an_studiu_update(self):
        test_an_studiu = An_Studiu.objects.get(an=5)
        test_an_studiu.an = 6
        test_an_studiu.save()
        self.assertEqual(test_an_studiu.an, 6)

    def test_an_studiu_deletion(self):
        test_an_studiu = An_Studiu.objects.get(an=5)
        test_an_studiu.delete()
        self.assertRaises(An_Studiu.DoesNotExist, An_Studiu.objects.get, an=5)
        self.assertRaises(An_Studiu.DoesNotExist, An_Studiu.objects.get, an=6)


class SemestruTestCase(TestCase):
    def setUp(self):
        Semestru.objects.create(nr_semestru=5)

    def test_semestru_creation(self):
        # Verificăm dacă obiectul de tip Grupa a fost creat cu succes în baza de date
        test_semestru = Semestru.objects.get(nr_semestru=5)
        self.assertEqual(test_semestru.nr_semestru, 5)

    def test_semestru_update(self):
        test_semestru = Semestru.objects.get(nr_semestru=5)
        test_semestru.nr_semestru = 6
        test_semestru.save()
        self.assertEqual(test_semestru.nr_semestru, 6)

    def test_semestru_deletion(self):
        test_semestru = Semestru.objects.get(nr_semestru=5)
        test_semestru.delete()
        self.assertRaises(Semestru.DoesNotExist, Semestru.objects.get, nr_semestru=5)
        self.assertRaises(Semestru.DoesNotExist, Semestru.objects.get, nr_semestru=6)

class SpecializareTestCase(TestCase):
    def setUp(self):
        Specializare.objects.create(nume="Test_Specializare")

    def test_specializare_creation(self):
        # Verificăm dacă obiectul de tip Grupa a fost creat cu succes în baza de date
        test_specializare = Specializare.objects.get(nume="Test_Specializare")
        self.assertEqual(test_specializare.nume, 'Test_Specializare')

    def test_specializare_update(self):
        test_specializare = Specializare.objects.get(nume="Test_Specializare")
        test_specializare.nume = "Test_Specializare_2"
        test_specializare.save()
        self.assertEqual(test_specializare.nume, 'Test_Specializare_2')

    def test_specializare_deletion(self):
        test_specializare = Specializare.objects.get(nume="Test_Specializare")
        test_specializare.delete()
        self.assertRaises(Specializare.DoesNotExist, Specializare.objects.get, nume='Test_Specializare')
        self.assertRaises(Specializare.DoesNotExist, Specializare.objects.get, nume='Test_Specializare_2')

class GrupaTestCase(TestCase):
    def setUp(self):
        self.specializare = Specializare.objects.create(nume='Specializare test')
        self.grupa = Grupa.objects.create(
            id_grupa='GRUPA01',
            an=3,
            grupa='A',
            subgrupa='1',
            link='https://exemplu.com',
            Specializare=self.specializare
        )

    def test_grupa_creation(self):
        # Verificăm dacă obiectul de tip Grupa a fost creat cu succes în baza de date
        self.assertEqual(Grupa.objects.count(), 1)

    def test_id_specializare(self):
        # Verificăm dacă metoda id_specializare funcționează așa cum este de așteptat
        self.assertEqual(self.grupa.id_specializare(), 'Specializare test')

    def test_grupa_update(self):
        # Actualizăm valoarea atributului "link"
        self.grupa.link = 'https://noul-link.com'
        self.grupa.save()

        # Verificăm dacă actualizarea a fost făcută cu succes
        updated_grupa = Grupa.objects.get(id_grupa="GRUPA01")
        self.assertEqual(updated_grupa.link, 'https://noul-link.com')

    def test_grupa_deletion(self):
        # Ștergem obiectul de tip Grupa
        self.grupa.delete()

        # Verificăm dacă obiectul a fost șters cu succes din baza de date
        self.assertEqual(Grupa.objects.count(), 0)

class MailTestCase(TestCase):
    def setUp(self):
        # Create two users for the test
        self.user = User.objects.create_user(
            username='testuser1',
            email='testuser1@example.com',
            password='testpassword1'
        )

        # Create a Date_Personale object associated with the user
        self.user1 = Date_Personale.objects.create(
            User=self.user,
            nume='Test User',
            sex='M',
            nationalitate='Romanian',
            cetatenie='Romanian',
            telefon='1234567890',
            adresa='Test Address'
        )
        self.user0 = User.objects.create_user(
            username='testuser0',
            email='testuser0@example.com',
            password='testpassword0'
        )

        # Create a Date_Personale object associated with the user
        self.user2 = Date_Personale.objects.create(
            User=self.user0,
            nume='Test User',
            sex='M',
            nationalitate='Romanian',
            cetatenie='Romanian',
            telefon='1234567890',
            adresa='Test Address'
        )
        # Create a mail object for the test
        self.mail = Mail.objects.create(
            titlu='Test Mail',
            receptor=self.user2,
            emitator=self.user1,
            continut='Test mail content'
        )

    def test_mail_creation(self):
        # Verify if the mail object was created successfully
        test_mail = Mail.objects.get(titlu='Test Mail')
        self.assertEqual(test_mail.titlu, 'Test Mail')
        self.assertEqual(test_mail.receptor, self.user2)
        self.assertEqual(test_mail.emitator, self.user1)
        self.assertEqual(test_mail.continut, 'Test mail content')

    def test_mail_update(self):
        # Update the mail object for the test
        test_mail = Mail.objects.get(titlu='Test Mail')
        test_mail.continut = 'Updated test mail content'
        test_mail.save()

        # Verify if the mail object was updated successfully
        updated_mail = Mail.objects.get(titlu='Test Mail')
        self.assertEqual(updated_mail.continut, 'Updated test mail content')

    def test_mail_deletion(self):
        # Delete the mail object for the test
        test_mail = Mail.objects.get(titlu='Test Mail')
        test_mail.delete()

        # Verify if the mail object was deleted successfully
        with self.assertRaises(Mail.DoesNotExist):
            Mail.objects.get(titlu='Test Mail')


