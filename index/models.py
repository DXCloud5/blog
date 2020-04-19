from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=32,default='title')
    content = models.TextField(null=True,blank=True)
    pub_time = models.DateTimeField(auto_now=True)
    author = models.TextField(null=True,blank=True)
    art_class = models.CharField(max_length=32,default='null')

    def __str__(self):
        return self.title