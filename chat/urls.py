from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('chat/<str:pk>/', views.chat, name="chat"),
    path('all-users/', views.allUser, name="all-users"),
    path('add-friend/', views.addFriend, name="add-friend"),
    path('accept-friend/', views.acceptFriend, name="accept-friend"),
]