from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver

# Create your models here.
GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

QUALIFICATION_CHOICES = (
        ('10th', '10th'),
        ('12th', '12th'),
        ('Graduate', 'Graduate'),
        ('Other', 'Other'),
    )

class Course(models.Model):
    name = models.CharField(max_length=50)
    id=models.AutoField(primary_key=True)
    no_of_students= models.IntegerField(default=0)
    created_at= models.DateTimeField(auto_now_add=True)
    def __str__(self):
       return self.name


# Enquiry Form for Student
class StudentEnquiry(models.Model):   

    SOURCE_CHOICES = (
        ('Newspaper', 'Newspaper'),
        ('Family', 'Family'),
        ('Student of institute', 'Student of institute'),
        ('Social Sites', 'Social Sites'),
        ('Banner', 'Banner'),
        ('Website', 'Website'),
    )
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    FatherHusband_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    mobile_number = models.CharField(max_length=15)
    guardian_phone_number = models.CharField(max_length=15)
    ParentHusband_occupation = models.CharField(max_length=50)
    academic_qualification = models.CharField(max_length=20, choices=QUALIFICATION_CHOICES)
    professional_qualification = models.CharField(max_length=50)
    institute_knowing = models.CharField(max_length=50, choices=SOURCE_CHOICES)
    enquiry_for_course=models.ManyToManyField(Course)
    admission_done=models.BooleanField(default=False)
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# different user models
class CustomUser(AbstractUser):
    user_type = (
        ('1','Admin'),
        ('2','Teacher'),
        ('3','Caller'),
        ('4','Student'),
    )
    user_type=models.CharField(default=1,choices=user_type,max_length=50)
   

class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    created_at= models.DateTimeField(auto_now_add=True)
    academic_qualification = models.CharField(max_length=20, choices=QUALIFICATION_CHOICES)
    professional_qualification = models.CharField(max_length=50)
    objects=models.Manager()
    

class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    teacher = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    #add mobile number
    address = models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    created_at= models.DateTimeField(auto_now_add=True)
    academic_qualification = models.CharField(max_length=20, choices=QUALIFICATION_CHOICES)
    professional_qualification = models.CharField(max_length=50)
    course=models.ManyToManyField(Course)
    objects=models.Manager()

    def __str__(self):
        return (self.name)
@receiver(post_delete, sender=Teacher)
def delete_user(sender, instance, **kwargs):
    User = get_user_model()
    try:
        user = User.objects.get(id=instance.teacher.id)
        user.delete()
    except User.DoesNotExist:
        pass

class Caller(models.Model):
    id=models.AutoField(primary_key=True)
    caller=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    created_at= models.DateTimeField(auto_now_add=True)
    academic_qualification = models.CharField(max_length=20, choices=QUALIFICATION_CHOICES)
    professional_qualification = models.CharField(max_length=50)
    objects=models.Manager()
    def __str__(self):
        return (self.name)
@receiver(post_delete, sender=Caller)
def delete_user(sender, instance, **kwargs):
    User = get_user_model()
    try:
        user = User.objects.get(id=instance.caller.id)
        user.delete()
    except User.DoesNotExist:
        pass


class Student(models.Model):
    name = models.CharField(max_length=100)
    student=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    FatherHusband_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    mobile_number = models.CharField(max_length=15)
    guardian_phone_number = models.CharField(max_length=15)
    ParentHusband_occupation = models.CharField(max_length=50)
    academic_qualification = models.CharField(max_length=20, choices=QUALIFICATION_CHOICES)
    professional_qualification = models.CharField(max_length=50)
    course_id=models.ManyToManyField(Course)
    adhar_card=models.CharField(max_length=10)
    objects=models.Manager()
    def __str__(self):
        return(self.name)
@receiver(post_delete, sender=Student)
def delete_user(sender, instance, **kwargs):
    User = get_user_model()
    try:
        user = User.objects.get(id=instance.student.id)
        user.delete()
    except User.DoesNotExist:
        pass


# class Session(models.Model):        
class Attendance(models.Model):
    course_id=models.ForeignKey(Course,on_delete=models.DO_NOTHING)
    student_id=models.ForeignKey(Student,on_delete=models.DO_NOTHING)
    date=models.DateField()
    created_at= models.DateTimeField(auto_now_add=True)





# # # class Courses(models.Model):