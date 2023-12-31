from django.db import models

# Create your models here.

class School(models.Model):
    school_name = models.CharField(max_length=100,primary_key=True)
    school_principal = models.CharField(max_length=100)
    school_location = models.CharField(max_length=100)
    
    def __str__(self):
        return self.school_name



class Student(models.Model):
    ## related_name='tushar' --> fetching information of child table without using child table but with the help parent table object
    school_name = models.ForeignKey(School, on_delete=models.CASCADE, related_name='tushar')
    student_name = models.CharField(max_length=100)
    student_age = models.IntegerField()
    
    def __str__(self):
        return self.student_name
