from django.db import models
from django.conf import settings

class Story(models.Model):
    title = models.CharField(max_length=200)
    characters = models.TextField()  # You can include multiple characters here
    ages = models.CharField(max_length=50, blank=True)  # New field for ages or age range
    setting = models.TextField()
    theme = models.CharField(max_length=100)
    content = models.TextField(blank=True)  # Generated content will be stored here
    illustration = models.ImageField(upload_to='stories/', null=True, blank=True)
    status = models.CharField(max_length=50, default='pending')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
