from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import auth, Group
from .models import UnivInfo, EventInfo
from Alumni_Interface.models import AlumniInfo
from .forms import UnivForm, EditForm, EventForm
from Alumni_Interface.decorator import unauthenticated_user, group_check


def register(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        group = Group.objects.get(name='University')
        user.groups.add(group)
        login(request, user)
        return redirect('/univ/UnivDetails/')
    else:
        form = UserCreationForm()

    return render(request, 'UnivSignup.html', {'form': form})


@unauthenticated_user
@group_check(allowed_roles=['University'])
def dashboard_view(request):
    events = EventInfo.objects.all()
    context = {
        'events':events
    }
    return render(request, 'udashboard.html', context)


@unauthenticated_user
@group_check(allowed_roles=['University'])
def profile_view(request): 
    dtl = UnivInfo.objects.get(user=request.user)
    context = {
        'nm': dtl.univ_name,
        'em': dtl.email,
        'te': dtl.tel,
        'ad': dtl.address,
        'pp': dtl.profile_pic,
    }
    return render(request, 'uprofile.html', context)


def logout(request):
    auth.logout(request)
    return redirect('login_')


def info_input(request):
    if request.method == 'POST':
        form = UnivForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('login_')
    
    else:
        form = UnivForm()

    context = {'form': form}
    return render(request, 'UnivDetails.html', context)


@unauthenticated_user
@group_check(allowed_roles=['University'])
def info_edit(request):
    dtl = UnivInfo.objects.get(user=request.user)
    if request.method == 'POST':
        dtl.email = request.POST["email"]
        dtl.tel = request.POST["tel"]
        dtl.address = request.POST["address"]
        dtl.profile_pic = request.POST["profilepic"]
        dtl.save()
        return redirect('profile')

    context = {
        'em': dtl.email,
        'te': dtl.tel,
        'ad': dtl.address,
        'pp': dtl.profile_pic,
    }
    return render(request, 'uEditDetails.html', context)


@unauthenticated_user
@group_check(allowed_roles=['University'])
def alumni_display(request):
    al = AlumniInfo.objects.all
    context = {
        'al': al
    }
    return render(request, 'alumni.html', context)


@unauthenticated_user
@group_check(allowed_roles=['University'])
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event')
    else:
        form = EventForm()
    context = {'form': form}
    return render(request, 'event.html', context)
    