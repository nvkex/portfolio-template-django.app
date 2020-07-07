from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length = 100)
    pubDate = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        if len(self.body) < 97:
            return self.body
        else:
            return self.body[0:97] +"..."