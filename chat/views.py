from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from django.shortcuts import render, redirect


from .models import Message


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'chat/login.html', context)


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return render(request, 'login.html')


@login_required(login_url='login/')
def index(request):
    return render(request, 'chat/index.html')


def room(request, room_name):
    room_name = 'chat'
    username = request.GET.get('username')
    messages = Message.objects.filter(room=room_name)[0:25]

    return render(request, 'chat/room.html', {'room_name': room_name, 'username': username, 'messages': messages})