from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse,Http404,HttpResponseRedirect

# Create your views here.
def index(request):
    try:
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
        current_user=request.user
        profile =Profile.objects.get(username=current_user)
    except ObjectDoesNotExist:
        return redirect('create-profile')
    return render(request,'index.html')

@login_required(login_url='/accounts/login/')
def notifications(request):
    current_user=request.user
    profile=Profile.objects.get(username=current_user)
    all_notifications = Notifications.objects.all()

    return render(request,'notification.html',{"all_notifications":all_notifications})

@login_required(login_url='/accounts/login/')
def dailyrecords(request):
    current_user = request.user
    profile = Profile.objects.get(username=current_user)
    all_dailyrecords=dailyrecords.objects.filter(locations=profile.locations)
    
    return render (request,'dailyrecords.html',{"dailyrecords":all_dailyrecords})

@login_required(login_url='/accounts/login/')
def my_profile(request):
    current_user=request.user
    records = Dailyrecords.objects.filter(username_id=current_user.id).all()
    return render(request,'profile/user_profile.html',{"records":records})


@login_required(login_url='/accounts/login/')
def user_profile(request,username):
    user = User.objects.get(username=username)
    profile =Profile.objects.get(username=user)
 
@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user=request.user
    if request.method=="POST":
        form =ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.username = current_user
            profile.save()
        return redirect('/')
    else:
        form = ProfileForm()
        return render(request,'profile/profile_form.html',{"form":form})
@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user=request.user
    if request.method=="POST":
        instance = Profile.objects.get(username=current_user)
        form =ProfileForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.username = current_user
            profile.save()

        return redirect('Index')

    elif Profile.objects.get(username=current_user):
        profile = Profile.objects.get(username=current_user)
        form = ProfileForm(instance=profile)
    else:
        form = ProfileForm()

    return render(request,'profile/update_profile.html',{"form":form})


@login_required(login_url='/accounts/login/')
def location(request):
    current_user=request.user
    profile=Profile.objects.get(username=current_user)
    all_location = Location.objects.filter(locations=profile.locations)

    return render(request,'locations.html',{"all_location":all_location})

@login_required(login_url='/accounts/login/')
def new_location(request):
    current_user=request.user
    profile =Profile.objects.get(username=current_user)

    if request.method=="POST":
        form =LocationForm(request.POST,request.FILES)
        if form.is_valid():
            business = form.save(commit = False)
            business.owner = current_user
            business.locations = profile.locations
            business.save()

        return HttpResponseRedirect('location')

    else:
        form = LocationForm()

    return render(request,'locations_form.html',{"form":form})