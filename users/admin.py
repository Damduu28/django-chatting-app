from django.contrib import admin

# Register your models here.
from .models import User, Friend
admin.site.register(User)
admin.site.register(Friend)
