from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import auth, Group
from .models import AlumniInfo
from Univ_Interface.models import EventInfo
from .forms import AlumniForm, EditForm
from .decorator import unauthenticated_user, group_check


def home_view(request):
    return render(request, 'home.html')


def register(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        group = Group.objects.get(name='Alumni')
        user.groups.add(group)
        login(request, user)
        return redirect('/alumniDetails/')
    else:
        form = UserCreationForm()

    return render(request, 'alumniSignup.html', {'form': form})

@unauthenticated_user
@group_check(allowed_roles=['Alumni'])
def dashboard_view(request):
    events = EventInfo.objects.all()
    context = {
        'events':events
    }
    return render(request, 'dashboard.html', context)

@unauthenticated_user
@group_check(allowed_roles=['Alumni'])
def profile_view(request):
    dtl = AlumniInfo.objects.get(user=request.user)
    context = {
        'nm': dtl.name,
        'rn': dtl.r_no,
        'em': dtl.email,
        'co': dtl.course,
        'mn': dtl.m_no,
        'on': dtl.org_name,
        'oa': dtl.org_add,
        'ad': dtl.al_dsg,
        'pp': dtl.profile_pic,
    }
    return render(request, 'profile.html', context)


def logout(request):
    auth.logout(request)
    return redirect('login_')


def info_input(request):
    if request.method == 'POST':
        form = AlumniForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('login_')
    
    else:
        form = AlumniForm()

    context = {'form': form}
    return render(request, 'AlumniDetails.html', context)

@unauthenticated_user
@group_check(allowed_roles=['Alumni'])
def info_edit(request):
    dtl = AlumniInfo.objects.get(user=request.user)
    if request.method == 'POST':
        dtl.email = request.POST["email"]
        dtl.course = request.POST["course"]
        dtl.m_no = request.POST["mno"]
        dtl.org_name = request.POST["orgname"]
        dtl.org_add = request.POST["orgadd"]
        dtl.al_dsg = request.POST["aldsg"]
        dtl.profile_pic = request.POST["profilepic"]
        dtl.save()
        return redirect('profile')

    context = {
        'em': dtl.email,
        'co': dtl.course,
        'mn': dtl.m_no,
        'on': dtl.org_name,
        'oa': dtl.org_add,
        'ad': dtl.al_dsg,
        'pp': dtl.profile_pic,
    }
    return render(request, 'EditDetails.html', context)