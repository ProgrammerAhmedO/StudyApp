from django.shortcuts import render
from .models import *


def home(request):
    q = request.GET.get('q') 
    if request.GET.get('q') != None:
    
        rooms = Room.objects.filter(name__icontains = q)
    else: 
        rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request,'try/home.html',context)


    
def room(request , pk):

    room = Room.objects.get(id=pk)
    context = {'room':room}

    return render(request,'try/room.html',context)