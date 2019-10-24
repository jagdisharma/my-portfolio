from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_data = models.DateTimeField()
    body = models.TextField(max_length=3000)
    image = models.ImageField(upload_to='blog_images/')