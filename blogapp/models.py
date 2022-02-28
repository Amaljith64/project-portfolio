from django.db import models

# Create your models here.

class BlogPost(models.Model):
    name = models.CharField(max_length=250)
    job = models.CharField(max_length=250)
    desc = models.TextField()
    img = models.ImageField(upload_to="images")
    phone = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.title