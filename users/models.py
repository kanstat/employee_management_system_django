from django.db import models

# Create your models here.


class department(models.Model):
    name = models.CharField(max_length=150, null=True)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class employee(models.Model):
    name = models.CharField(max_length=150)
    dept = models.ForeignKey(department, on_delete=models.CASCADE, blank=True)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.CharField(max_length=200)
    hire_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return (f"({self.name} {self.dept})")
