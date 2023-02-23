from django.db import models

# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length=50)
	studyonline_id = models.CharField(max_length=50)
	dob = models.DateField()
	mail_id = models.EmailField()
	phone_no = models.CharField(max_length=50)
	branch = models.CharField(max_length=50)


    