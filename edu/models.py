from django.db import models

# Create your models here.
class alumni_info(models.Model):
    student_name=models.CharField(max_length=70)
    college=models.CharField(max_length=70)
    def __str__(self) :
        return self.student_name