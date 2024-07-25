from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def home_view(request):
    if (request.method == 'POST'):
        username = request.POST["username"]
        room = request.POST["room"]
        try:
            existingRoom = Room.objects.get(room_name__icontains=room)
        except Room.DoesNotExist:
            r = Room.objects.create(room_name=room)
        return redirect("room", room_name=room, username=username)
            
    return render(request, 'home.html')

def room_view(request, room_name, username):
    existingRoom = Room.objects.get(room_name__icontains=room_name)
    get_messages = Message.objects.filter(room=existingRoom)
    context = {
        "messages" : get_messages,
        "room" : existingRoom.room_name,
        "user" : username
    }
    return render(request, 'room.html', context)