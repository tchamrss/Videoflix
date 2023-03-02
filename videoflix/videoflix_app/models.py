from django.db import models
from datetime import date

# Create your models here.


class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    created_at =  models.DateField(default=date.today)
    video_file = models.FileField(upload_to='videos', blank=True, null=True)
    
    def __str__(self):
        return self.title