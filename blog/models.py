from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_data = models.DateTimeField()
    body = models.TextField(max_length=3000)
    image = models.ImageField(upload_to='blog_images/')

    def __str__(self):
        return self.title[:100]

    def summary(self):
        return self.body[:220]