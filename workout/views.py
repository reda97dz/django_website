from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Run
from .forms import RunForm, LoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def user_logout(request):
    logout(request)
    # return HttpResponseRedirect('login/')

def user_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = authenticate(request,
                                    username=cd['username'],
                                    password=cd['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return HttpResponseRedirect('/')
                    else:
                        return HttpResponse('Disabled Account')
                else:
                    return HttpResponse('Invalid Input')
        else:
            form = LoginForm()    
        
    return render(request, 'workout/login.html', {'form': form})

def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save() 
            return render(request,
                          'workout/register_done.html',
                          {'new_user': new_user})   
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'workout/register.html',
                  {'user_form': user_form})

@login_required(login_url='login/')
def run_list(request, year=None, month=None):
    runs = Run.objects.filter(user=request.user)
    
    if year:
        runs = Run.objects.filter(date__year=year)
    if month:
        runs = Run.objects.filter(date__year=year,date__month=month)
    
    return render(request,
                  'workout/run/list.html',
                  {'runs': runs,
                   'year': year,
                   'month': month})

@login_required(login_url='login/')
def run_details(request, pk):
    run = Run.objects.get(id=pk, user=request.user)
    return render(request,
                  'workout/run/details.html',
                  {'run': run})

@login_required(login_url='login/')
def add_run(request):
    if request.method == 'POST':
        form = RunForm(data=request.POST)
        if form.is_valid():
            distance = form.cleaned_data['distance']
            duration = form.cleaned_data['duration']
            pace = float(duration)/float(distance)
            new_run = form.save(commit=False)
            new_run.pace = pace
            new_run.user = request.user
            new_run.save()
        return redirect('/run/{}'.format(new_run.id))
    else:
        form = RunForm()
    
    return render(request, 
                  'workout/run/addrun.html',
                  {'form':form})

@login_required(login_url='login/')
def delete_run(request, pk):
    run = Run.objects.get(id=pk,user=request.user)
    if request.method == 'POST':
        run.delete()
        return redirect('/workout/')
    
    return render(request, 
                  'workout/run/deleterun.html', 
                  {'run': run})

@login_required(login_url='login/')
def edit_run(request, pk):
    run = Run.objects.get(id=pk)
    
    if request.method == 'POST':
        form = RunForm(request.POST, instance=run)
        if form.is_valid():
            pace = float(form.cleaned_data['duration'])/float(form.cleaned_data['distance'])
            edit_run = form.save(commit=False)
            edit_run.pace = pace
            edit_run.save()
        return redirect('/run/{}'.format(edit_run.id))
    else:
        form = RunForm(instance=run)
    
    return render(request,
                  'workout/run/editrun.html',
                  {'form': form,
                   'run': run})