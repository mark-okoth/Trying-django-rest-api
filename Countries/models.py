from django.db import models

# Create your models here.
class Countries(models.Model):
    name = models.CharField(max_length=20)
    Location = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    