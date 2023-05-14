# Generated by Django 4.1.4 on 2023-05-06 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='An_Studiu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('file_backup', models.DecimalField(decimal_places=0, default=0, max_digits=2)),
            ],
            options={
                'verbose_name_plural': 'ani_studiu',
                'db_table': 'an_studiu',
            },
        ),
        migrations.CreateModel(
            name='Date_Personale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=1)),
                ('nationalitate', models.CharField(max_length=50)),
                ('cetatenie', models.CharField(max_length=50)),
                ('data_nasterii', models.DateTimeField(auto_now_add=True)),
                ('telefon', models.CharField(max_length=10)),
                ('adresa', models.CharField(max_length=200)),
                ('adresa_mail', models.CharField(max_length=50)),
                ('CNP', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('an_studiu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.an_studiu')),
            ],
            options={
                'verbose_name_plural': 'Date_Personale',
                'db_table': 'date_personale',
            },
        ),
        migrations.CreateModel(
            name='Grupa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id_grupa', models.CharField(max_length=50)),
                ('file_backup', models.DecimalField(decimal_places=0, max_digits=100)),
                ('grupa', models.CharField(max_length=50)),
                ('subgrupa', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Grupe',
                'db_table': 'grupa',
            },
        ),
        migrations.CreateModel(
            name='Materie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nume', models.CharField(max_length=50)),
                ('credite', models.DecimalField(decimal_places=0, max_digits=100)),
            ],
            options={
                'verbose_name_plural': 'Materii',
                'db_table': 'materie',
            },
        ),
        migrations.CreateModel(
            name='Materiile_Grupelor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ID_mat_grupa', models.DecimalField(decimal_places=0, max_digits=100)),
                ('Grupa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.grupa')),
                ('Materie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.materie')),
            ],
            options={
                'verbose_name_plural': 'materiile_grupelor',
                'db_table': 'materiile_grupelor',
            },
        ),
        migrations.CreateModel(
            name='Semestru',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nr_semestru', models.DecimalField(decimal_places=0, default=0, max_digits=2)),
            ],
            options={
                'verbose_name_plural': 'semestre',
                'db_table': 'semestru',
            },
        ),
        migrations.CreateModel(
            name='Specializare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nume', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Specializari',
                'db_table': 'specializare',
            },
        ),
        migrations.CreateModel(
            name='Noutati',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titlu', models.CharField(max_length=50)),
                ('anunt', models.CharField(max_length=200)),
                ('adresa_mail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.date_personale')),
            ],
            options={
                'verbose_name_plural': 'Noutati',
                'db_table': 'noutati',
            },
        ),
        migrations.CreateModel(
            name='Note_Materie_Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('Date_Personale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.date_personale')),
                ('Materiile_Grupelor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.materiile_grupelor')),
            ],
            options={
                'verbose_name_plural': 'Note_materii_student',
                'db_table': 'note_materie_student',
            },
        ),
        migrations.CreateModel(
            name='Materiile_Profesorului',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('titlu', models.CharField(max_length=50)),
                ('CNP_profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.date_personale')),
                ('materie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.materie')),
            ],
            options={
                'verbose_name_plural': 'Materiile Profesorului',
                'db_table': 'materiile_profesorului',
            },
        ),
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('titlu', models.CharField(max_length=50)),
                ('continut', models.CharField(max_length=200)),
                ('emitator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emitator', to='hr.date_personale')),
                ('receptor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receptor', to='hr.date_personale')),
            ],
            options={
                'verbose_name_plural': 'mailuri',
                'db_table': 'mail',
            },
        ),
        migrations.AddField(
            model_name='grupa',
            name='Specializare',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.specializare'),
        ),
        migrations.AddField(
            model_name='date_personale',
            name='semestru',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.semestru'),
        ),
    ]
