from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
        
    def __str__(self):
	    return self.name


class Tag(models.Model):
    name = models.CharField(max_length=65, unique=True)

    def __str__(self):
        return self.name
    

class Resources(models.Model):
    title = models.CharField(max_length=75)
    description = models.TextField(max_length=250)
    file = models.FileField(upload_to='resources/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='resources')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resources')
    tags = models.ManyToManyField(Tag, blank=True, related_name='resources') 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
    	return self.title

# Create your models here.