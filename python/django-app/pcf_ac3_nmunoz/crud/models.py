from django.db import models

# Create your models here.
class Usuario(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=200, unique=True)

    def __str__(self):
        return f'{self.id} - {self.name} - {self.email}'
