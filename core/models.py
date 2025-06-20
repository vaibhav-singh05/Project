from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=50)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.city}"
