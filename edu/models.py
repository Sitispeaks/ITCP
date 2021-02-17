from django.db import models

# Create your models here.
class alum(models.Model):
    stu_name=models.CharField(max_length=70)
    college=models.CharField(max_length=70)
    def __str__(self) :
        return self.stu_name