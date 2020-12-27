from django.db import models

# Create your models here.
class News(models.Model):
    pdf = models.FileField()
    title = models.CharField(max_length=30)
    head = models.CharField(max_length=250)
    slug = models.SlugField()
    text = models.TextField()
    data = models.DateTimeField(auto_now_add=True)