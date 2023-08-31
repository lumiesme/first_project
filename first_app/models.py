from django.db import models
from django.contrib import admin

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    """ kommentaari saab kirjutada nii """
    date_of_birth = models.DateField(null=True, blank=True)  # sünniaeg võib jääda tühjaks- vt sulgusid
    weight = models.IntegerField()

class StudentAdmin(admin.ModelAdmin):
    list_filter = ['weight']

    #@admin.display(description='birthday')
    def birthday(self, obj):
        # Stakoverflow 7216764 Change data format on admin page
        if obj.date_of_birth is not None:
            return obj.date_of_birth.strftime('%d.%m.%Y')


    list_display = ['name', 'birthday', 'weight']      # nii nagu siia kirjutad, täpselt samas jrk tuleb ka lehel need tulemused
    list_per_page = 10


class Teacher(models.Model):  # kui topelt kirj.teachers siis tuleb tabelisse teacherss
    name = models.CharField(max_length=100)
    """ kommentaari saab kirjutada nii """
    subject = models.CharField(max_length=100)
class TeachersAdmin(admin.ModelAdmin):

    list_display = ['name', 'subject']      # nii nagu siia kirjutad, täpselt samas jrk tuleb ka lehel need tulemused
    #list_per_page = 10
class Subject(models.Model):
    subject = models.CharField(max_length=100)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subject']
