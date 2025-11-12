# from django.db import models
# from django.contrib.auth.models import User

# # Create your models here.
# class Department(models.Model):
#     name = models.CharField(max_length=100)
#     location = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# class Role(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# class Employee(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # who added this record
#     first_name = models.CharField(max_length=100, null=False)
#     last_name = models.CharField(max_length=100, blank=True)
#     dept = models.ForeignKey(Department, on_delete=models.CASCADE)
#     salary = models.IntegerField(default=0)
#     bonus = models.IntegerField(default=0)
#     role = models.ForeignKey(Role, on_delete=models.CASCADE)
#     phone = models.BigIntegerField(default=0)
#     hire_date = models.DateField()

#     def __str__(self):
#         return f"{self.first_name} {self.last_name} ({self.phone})"
from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='employees')
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, blank=True)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='employees')
    phone = models.CharField(max_length=15, default='0')  # safer than BigIntegerField
    hire_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.phone})"
