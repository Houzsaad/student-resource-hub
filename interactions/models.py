from django.db import models
from resources.models import Resources, Category
from django.contrib.auth import get_user_model

User = get_user_model()

class Rating(models.Model):
    resource = models.ForeignKey(Resources, on_delete=models.CASCADE, related_name='resource')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    score = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['resource', 'user']

    def __str__(self):
        return f'{self.user} rated {self.resource} - {self.score}'
    
class Comment(models.Model):
    resource = models.ForeignKey(Resources, on_delete=models.CASCADE, related_name='comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    body = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} on {self.resource}'
    
class  Notification(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notification')
    message = models.CharField(max_length=200)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Notification for {self.owner}'


#Create your models here.
