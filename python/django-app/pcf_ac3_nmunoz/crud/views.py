from .models import Usuario
from django.shortcuts import redirect, render
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def read_users(request):
    users = User.objects.all()
    context = {'users': users}

    return render(request, 'read_users.html', context=context)

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    form = UserForm

    context = {'form': form}

    return render(request, 'create_user.html', context=context)

def update_user(request, id):
    if request.method == 'POST':
        user = User.objects.get(id=id)

        form = UserForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            return redirect('index')

    form = UserForm

    context = {'form': form}

    return render(request, 'update_user.html', context=context)

def detele_user(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('read')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username, password)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Invalid username or password')

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('login')
