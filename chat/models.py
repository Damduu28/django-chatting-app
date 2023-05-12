from django.db import models
from users.models import User

# Create your models here.

class Chat(models.Model):
    sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="receiver", on_delete=models.CASCADE)
    message = models.TextField(max_length=1024)
    created = models.DateTimeField(auto_now_add=True)
    is_seen =  models.BooleanField(default=False)
    
    def __str__(self):
        return self.message
    
    class Meta:
        ordering = ["-created"]