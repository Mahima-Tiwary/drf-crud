from django.db import models

class Student(models.Model):
    s_id = models.IntegerField(primary_key=True,default=0)
    username = models.CharField(max_length=20, unique= True)
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=60)
    college = models.CharField(max_length=100)
    branch = models.CharField(max_length=50)


# Create your models here.
