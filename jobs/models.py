from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length = 100, default = "Project Title")
    giturl = models.TextField(default = "/")
    url = models.TextField(default = "/")
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length = 200)
