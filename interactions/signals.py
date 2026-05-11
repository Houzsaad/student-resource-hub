from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Rating, Comment, Notification

@receiver(post_save, sender=Rating)
def notify_on_rating(sender, instance , created, **kwargs):
    if created:
        Notification.objects.create(
            owner=instance.resource.uploaded_by,
            message=f'{instance.user.full_name} rated on your resource "{instance.resource.title}" {instance.score} starts'
        )

@receiver(post_save, sender=Comment)
def notify_on_comment(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            owner=instance.resource.uploaded_by,
            message=f'{instance.user.full_name} commented on your resource "{instance.resource.title}"'
        )