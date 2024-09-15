from django.db import models

from userprofile.models import UserProfile


class Client(models.Model):
    GENDER_CHOICES = [
        ('Mr.', 'Mister'),
        ('Ms.', 'Miss')
    ]

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    gender = models.CharField(max_length=3, choices=GENDER_CHOICES)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=8)

    def __str__(self):
        return f"{self.get_gender_display()} {self.first_name} {self.last_name}"
