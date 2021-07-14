from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserForm


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, "Username or password is incorrect")
    context = {}
    return render(request, 'users/login_register.html', context)


def logoutUser(request):
    logout(request)
    messages.error(request, "User was Logged out")
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "New user account was created ")

            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, "An error occurred while creating")

    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)


def profile(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    topskills = profile.skill_set.exclude(description__exact=" ")
    otherskills = profile.skill_set.filter(description__exact="")
    context = {'profile': profile, 'topskills': topskills,
               'otherskills': otherskills}
    return render(request, 'users/user-profile.html', context)
