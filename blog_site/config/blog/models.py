from django.db import models
from django.urls import reverse
from datetime import datetime
# Create your models here.

class Post(models.Model):
    
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete= models.CASCADE )
    body = models.TextField()
    date = models.DateTimeField(default=datetime.now)
    def sample(self):
        return self.body[:500]
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('details',args=[str(self.id)])