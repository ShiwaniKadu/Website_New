from django.db import models

# Create your models here.
class Recepie(models.Model):
    receipe_name = models.CharField(max_length=100)
    receipe_decription = models.TextField()
    receipe_image = models.ImageField(uplaod_to="receipe")
    