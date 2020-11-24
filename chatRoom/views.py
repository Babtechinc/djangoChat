from .models import ChatModel
from django.shortcuts import render


def index(request):

    return render(request,'index.html',context={})

def room(request,room_name):
    room_group_name = 'chat_%s' % room_name
    ChatS = ChatModel.objects.filter(room=room_group_name).order_by('id')
    return render(request,'chatRoom.html',context={'Room':room_name,'RoomChat':ChatS})