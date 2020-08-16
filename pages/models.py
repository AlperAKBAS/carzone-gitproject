from django.db import models
from django.utils import timezone
from PIL import Image

# Create your models here.
class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    facebook_link = models.URLField(max_length=150)
    twitter_link = models.URLField(max_length=150)
    google_plus_link = models.URLField(max_length=150)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Staff: {self.first_name} {self.last_name} - {self.designation}'

    def save(self, *args, **kwargs):
        ### IMAGE RESIZE
        super().save(*args, **kwargs)
        img = Image.open(self.photo.path)
        if img.height > 600 or img.width > 600:
            output_size = (600,600)
            img.thumbnail(output_size)
            img.save(self.photo.path)