from django.db import models
from django.contrib.auth.models import AbstractUser

from uuid import uuid4
import os

# Create your models here.

def avatar_upload_path(instance, filename):
    upload_to = "profile"
    ext = filename.split('.')[1]
    
    if instance.pk:
        filename = "{}.{}".format(instance.pk, ext)
    else:
        filename = "{}.{}".format(uuid4().hex, ext)
    return os.path.join(upload_to, filename)

# class UserManager(models.Manager):
#     def get_all_user(self):
#         return self.all()

class User(AbstractUser):
    friends = models.ManyToManyField('User', blank=True)
    name = models.CharField(max_length=255)
    email  = models.EmailField(max_length=254, unique=True)
    status = models.CharField(default="Not Active", max_length=50)
    avatar = models.ImageField(upload_to=avatar_upload_path, default="avatar.png", null=True)
    
    # objects = UserManager()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.username
    
    @property
    def get_avatar_url(self):
        return self.avatar.url
    
    @property
    def get_user_name(self):
        if not self.name:
            uname = self.username
        else:
            uname = self.name
        return uname
            
    
class Friend(models.Model):
    from_user = models.ForeignKey(User, related_name="from_user", on_delete=models.CASCADE)
    to_friend = models.ForeignKey(User, related_name="to_friend", on_delete=models.CASCADE)
    is_request = models.BooleanField(default=False, null=True, blank=True)
    
    def __str__(self):
        return "from {} to {}".format(self.from_user, self.to_friend)
    
    
