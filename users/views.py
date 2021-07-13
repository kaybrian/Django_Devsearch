from django.shortcuts import render
from .models import Profile


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
