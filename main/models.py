from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Users(AbstractUser):
    position = models.CharField(max_length=30)
    phone = models.CharField(max_length=30, null=True)
    image = models.ImageField(upload_to='images/users')
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

class Kelish(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.date}"

class Ketish(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.date}"
    

class Ish_vaqti(models.Model):
    ishkelish = models.TimeField()
    ishketish = models.TimeField()