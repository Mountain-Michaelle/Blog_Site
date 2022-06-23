from tkinter import Image
from django.db import models
from django.conf import settings
from django.utils.text import slugify 
# Create your models here.
class Images(models.Model):
    users = models.ForeignKey(settings.AUTH_USER_MODEL,
                                related_name='images_created', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True) 

    url = models.URLField()
    images = models.ImageField(upload_to='images/%Y/%m/%d/')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True, db_index=True)

    
    def save(self, *args, **kwargs):
    #Overriding the save method 
        if not self.slug: 
            self.slug = slugify(self.title)
        super(Image, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    
        