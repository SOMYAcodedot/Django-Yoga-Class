from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    enrollment_date = models.DateField(null=True, blank=True)  # Nullable field

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Staff(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=50, null=True, blank=True)  # Nullable field

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
