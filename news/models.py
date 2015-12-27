from django.db import models
from django.utils import timezone



class Post(models.Model):
    HOME = 'Home'
    VALUES = 'Values'
    COME = 'Come'
    PARTICIPATE = 'Participate'
    CONTACT = 'Contact'
    ACTIVITY = 'Activity'
    LINK_CHOICES = (
        (HOME, 'Home'),
        (VALUES, 'Values'),
        (PARTICIPATE, 'Participate'),
        (COME, 'Come'),
        (CONTACT, 'Contact'),
        (ACTIVITY, 'Activity'),
    )
    link = models.CharField(max_length=24,choices=LINK_CHOICES,default=HOME)
    author = models.ForeignKey('auth.User')
    title = models.CharField(blank=True, null=True, max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
