from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model

class Message(models.Model):
    username = models.CharField(max_length=255)
    #username = models.ForeignKey(User, on_delete=models.CASCADE, default=User, null=False)
    room = models.CharField(max_length=255)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)

    def __str__(self):
        return f"{self.content}"