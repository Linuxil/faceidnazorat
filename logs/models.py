from django.db import models
from main.models import Employees
# Create your models here.

class Logs(models.Model):
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    enter = models.DateTimeField(auto_now_add=True)
    exity = models.DateTimeField(null=True)