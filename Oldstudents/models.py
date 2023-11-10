from django.db import models
# from  django.contrib.auth.models import User



# Create your models here.
class Student(models.Model):
    student_number = models.PositiveBigIntegerField()
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.CharField(max_length=100)
    field_of_work = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    telephone_number = models.CharField(max_length=15, null=True, blank=True)
    YEAR_CHOICES = [(year, year) for year in range(2000, 2030)]  # Adjust the range as needed

    year_of_entry = models.IntegerField(choices=YEAR_CHOICES)
    year_of_completion = models.IntegerField(choices=YEAR_CHOICES)


    def __str__(self):
        return f'Student: {self.first_name} {self.last_name}'  