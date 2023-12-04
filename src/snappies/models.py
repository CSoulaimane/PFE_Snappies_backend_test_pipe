from django.db import models

# Create your models here.

class Commande(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    value = models.CharField(max_length=100)


    def __str__(self):
        return self.value