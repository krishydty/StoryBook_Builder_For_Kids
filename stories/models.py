from django.db import models
from django.conf import settings

class Story(models.Model):
    title = models.CharField(max_length=200)
    characters = models.TextField()
    theme = models.CharField(max_length=100)
    setting = models.TextField()
    content = models.TextField(blank=True)  # Generated content to be filled later
    illustration = models.ImageField(upload_to='stories/', null=True, blank=True)
    status = models.CharField(max_length=50, default='pending')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
