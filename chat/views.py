from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
from django.db.models import Q
from .utils import LazyEncode
import json

from users.models import User, Friend
from .models import Chat

# Create your views here.
@login_required(login_url="login")
def home(request):
    user = request.user
    new_users = User.objects.all()
    all_friends = user.friends.all()
    friend_requests = Friend.objects.filter(to_friend=user)
    last_chat = []
    for receiver in all_friends:
        chat = Chat.objects.filter(
        Q(sender=user) & Q(receiver=receiver)  |
        Q(sender=receiver) & Q(receiver=user)
        ).first()
        last_chat.append(chat)
    context = {"page": "home",
        "new_users": new_users, 
        "all_friends": all_friends, 
        "last_chat": last_chat, 
        "friend_requests": friend_requests, }
    return render(request, "chat/home.html", context)

@login_required(login_url="login")
def chat(request, pk):
    receiver = User.objects.get(id=pk)
    sender = request.user
    if request.method == "POST":
        chat = Chat.objects.create(
            sender=request.user,
            receiver=receiver,
            message=request.POST.get('message')
        )
    
    chats = Chat.objects.filter(
        Q(sender=sender) & Q(receiver=receiver)  |
        Q(sender=receiver) & Q(receiver=sender)
        ).order_by('id')
    context = {'chats': chats}
    return render(request, "chat/chat.html", context)

def addFriend(request):
    user_from = request.user
    data = json.loads(request.body)
    userId = data['userId']
    action = data['action']
    to_friend = User.objects.get(id=userId)
    
    if action == "add":
        friend, created = Friend.objects.get_or_create(
            from_user=user_from,
            to_friend=to_friend,
            is_request=True
        )
    elif action == 'cancel':
        friend = Friend.objects.get(
            from_user=user_from,
            to_friend=to_friend
        )
        friend.delete()
    
    return JsonResponse('adding friend...', safe=False)

def acceptFriend(request):
    data = json.loads(request.body)
    requestId = data['requestId']
    action = data['action']
    
    friend = Friend.objects.get(id=requestId)
    if action == "confirm":
        if friend.to_friend == request.user:
            friend.to_friend.friends.add(friend.from_user)
            friend.from_user.friends.add(friend.to_friend)
            friend.delete()
    elif action == 'delete':
        friend.delete()
        
    return JsonResponse('accepting or deleting friend request...', safe=False)
    
def allUser(request):
    users = User.objects.get_all_user()
    users = serialize('json', users)
    new_users = []
    name = ''
    for i in range(len(users)):
        pass
        # print(users[i].filed)
    #     new_users.append({"id": user.pk, "name": user.name, 'image': user.avatar})
    # print(users)
    return JsonResponse(json.loads(users), safe=False)
