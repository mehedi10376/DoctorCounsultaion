from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_sex = (('MALE', 'Male'), ('FEMALE', 'Female'))
    user_gender = models.CharField(max_length=6, default='Male', choices=user_sex)
    user_age = models.IntegerField(null=True)
    user_phone = models.CharField(max_length=200, null=True)
    user_address = models.CharField(max_length=200, null=True)
    user_email = models.CharField(max_length=200, null=True)
    user_img = models.ImageField(upload_to='profile_pics', default='default.jpg')
    is_doctor = models.BooleanField(default = False)

    def __str__(self):
        return self.user.username

class Department(models.Model):
    dept_name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.dept_name

class Doctor(models.Model):
    doc_name =models.OneToOneField(User, on_delete=models.CASCADE)
    doc_department = models.ForeignKey(Department, null=True, on_delete= models.SET_NULL)
    starting_time = models.CharField(max_length=200, null=True)
    ending_time = models.CharField(max_length=200, null=True)
    sat_day= models.BooleanField(default = False)
    sun_day= models.BooleanField(default = False)
    mon_day= models.BooleanField(default = False)
    tues_day= models.BooleanField(default = False)
    wed_day= models.BooleanField(default = False)
    thurs_day= models.BooleanField(default = False)
    fri_day= models.BooleanField(default = False)
    

def __str__(self):
    return self.doc_name.username