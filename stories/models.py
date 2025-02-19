# stories/models.py
from django.db import models
from django.conf import settings

class Story(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]
    
    title = models.CharField(max_length=200)
    characters = models.TextField()
    theme = models.CharField(max_length=100)
    setting = models.TextField()
    content = models.TextField(blank=True)            # AI-generated story text
    illustration_url = models.URLField(blank=True)      # URL for generated image
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
