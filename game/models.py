from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.URLField()  # To store the Wikipedia image URL
    
    def __str__(self):
        return self.name
