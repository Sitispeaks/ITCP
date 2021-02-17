from django.db import models
from django.utils import timezone
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=70)
    surname = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    phone = models.CharField(max_length=11)
    messages = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# from django.db import models

# specifying choices

SEMESTER_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
)

# declaring a Student Model


class Student(models.Model):
    semester = models.CharField(max_length=20, choices=SEMESTER_CHOICES, default="1")



Batches=(
    ("+2 1st Year","+2 1st Year"),
    ("+2 2nd Year","+2 2nd Year"),
    ("+3 1st Year","+3 1st Year"),
    ("+3 2nd Year","+3 2nd Year"),
    ("+3 3rd Year","+3 3rd Year"),
)

class Note(models.Model):
    desc=models.CharField(max_length=70)
    notes=models.FileField(upload_to='media')
    date_posted = models.DateTimeField(default=timezone.now)
    batch=models.CharField(max_length=30,choices=Batches,default="+2 1st Year")



class Holiday(models.Model):
    holiday=models.CharField(max_length=100)
    def __str__(self):
        return str(self.holiday)