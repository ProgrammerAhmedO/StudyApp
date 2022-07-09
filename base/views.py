from multiprocessing import context
from venv import create
from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from .forms import RoomForm, messageForm
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
# rooms = [
#     {'id' : 1 , 'name':'this is first room'},
#     {'id' : 2 , 'name':'this is 2nd room'},
#     {'id' : 3 , 'name':'this is 3rd room'}
# ]

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Your account dosent exist')


        user = authenticate(request, username=username , password=password)
        if user != None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'user name or password is wrong !')

    context = {}
    return render (request , 'base/login_register.html',context)



def logoutuser(request):
    logout(request)
    return redirect('home')



def home(request):
    
    topics = Topic.objects.all()
    q = request.GET.get('q') if request.GET.get('q') != None else '' #the Q method didn't take None as paramiter 
    topics_count = topics.count()
    rooms = Room.objects.filter(Q(topic__name__icontains=q) | Q(name__icontains=q) |Q(description__icontains=q)|Q(Host__username__icontains=q))
    room_messaes = message.objects.filter(Q(room__topic__name__icontains=q))
    

    context = {
        
        'rooms':rooms,
        'topics':topics,
        'room_messaes':room_messaes,
        'topics_count':topics_count
        }
    return render(request,'base/home.html',context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    messages = room.message_set.all()
    Participants = room.participants.all()
    if request.method == 'POST':
        message.objects.create(
        user = request.user,
        room = room,
        body = request.POST.get('body')
    )
        room.participants.add(request.user)
        return redirect('room', pk = room.id)

           
    context = {
    'room':room,
    'msg':messages,
    'Participants':Participants
    
    }
    return render(request,'base/room.html', context)



@login_required(login_url='login')
def CreateRoom(request):
    Form = RoomForm()
    if request.method == 'POST':        
        Form = RoomForm(request.POST)
        if Form.is_valid:
            Room=Form.save(commit=False)
            Room.Host = request.user   
            Room.save()
            return redirect('home')

    context = {'Form':Form}
    return render(request, 'base/CreateRoom.html' , context)



@login_required(login_url='login')
def UpdateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.user != room.Host:
        return HttpResponse('you are not allawed to be here ')
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid :
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'base/UpdateRoom.html' , context)


@login_required(login_url='login')
def DeleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.user != room.Host:
        return HttpResponse('you are not allawed to be here ')
    if request.method == "POST":
            room.delete()
            return redirect('home')
    context = {'obj':room}
    return render(request, 'base/DeleteRoom.html' , context)


def profile(request,pk):
    currentuser = User.objects.get(id=pk)
    rooms = Room.objects.filter(Host__username = currentuser.username)

    topics = Topic.objects.all()
    q = request.GET.get('q') if request.GET.get('q') != None else '' #the Q method didn't take None as paramiter 
    
    total_rooms = Room.objects.filter(Q(topic__name__icontains=q) | Q(name__icontains=q) |Q(description__icontains=q)|Q(Host__username__icontains=q))
    room_messaes = message.objects.filter(user__id=currentuser.id)
    room_count = rooms.count()
    context={'currentuser':currentuser, 'rooms':rooms , 'room_count':room_count,
        'rooms':rooms,
        'topics':topics,
        'room_messaes':room_messaes,
        'total_rooms':total_rooms
        }
    return render(request, 'base/profile.html',context )

def deleteMessage(request,pk):
    Message = message.objects.get(id=pk)
    room = Room.objects.get(message__id =pk)
    
    if request.method == 'POST':
        Message.delete()
        return redirect('/')
    context = {'Message':Message}
    return render(request,'base/delete-message.html',context)

def updateMessage(request,pk):
    msg = message.objects.get(id=pk)
    Form = messageForm(instance=msg)
    if request.method == 'POST':
        if Form.is_valid:
            Form = messageForm(request.POST,instance=msg)
            Form.save()
            return redirect('/')
    context ={'Form':Form}
    return render(request, 'base/updateMessage.html',context)

def deleteActivites(request,pk):
    activity = message.objects.get(id=pk)
    if request.method == 'POST':
        activity.delete()
        return redirect('/')
    context = {'activity':activity}
    return render(request, 'base/deleteActivites.html', context)