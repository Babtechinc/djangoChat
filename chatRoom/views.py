from .models import ChatModel
import random
from django.shortcuts import render


def index(request):

    return render(request,'index.html',context={})

def room(request,room_name):
    room_group_name = 'chat_%s' % room_name
    ChatS = ChatModel.objects.filter(room=room_group_name).order_by('id')
    password_length = 5
    possible_characters = "1234567890"
    random_character_list = [random.choice(possible_characters) for i in range(password_length)]
    user = "".join(random_character_list)
    user  = "User" + user
    return render(request,'Chat.html',context={'Room':room_name,'RoomChat':ChatS,'user':user})

