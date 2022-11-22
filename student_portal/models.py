from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    fees = models.PositiveIntegerField()
    duration = models.PositiveIntegerField()
    is_active = models.BooleanField()

class Batches(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    batch_code = models.PositiveIntegerField()
    started_data = models.DateField()
    is_active = models.BooleanField()

class Students(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField()
    profile_pic = models.ImageField(upload_to='images')
    resume = models.FileField()
    qualification = models.CharField(max_length=200)
    batch = models.ForeignKey(Batches, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100)

class Placements(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    company = models.CharField(max_length=200)
