from django.shortcuts import render, redirect
from .models import Run
from .forms import RunForm

# Create your views here.
def run_list(request):
    runs = Run.objects.all()
    return render(request,
                  'workout/run/list.html',
                  {'runs': runs})

def run_details(request, pk):
    run = Run.objects.get(id=pk)
    return render(request,
                  'workout/run/details.html',
                  {'run': run})

def add_run(request):
    if request.method == 'POST':
        form = RunForm(data=request.POST)
        if form.is_valid():
            distance = form.cleaned_data['distance']
            duration = form.cleaned_data['duration']
            pace = float(duration)/float(distance)
            new_run = form.save(commit=False)
            new_run.pace = pace
            new_run.save()
        return redirect('/workout/run/{}'.format(new_run.id))
    else:
        form = RunForm()
    
    return render(request, 
                  'workout/run/addrun.html',
                  {'form':form})

def delete_run(request, pk):
    run = Run.objects.get(id=pk)
    if request.method == 'POST':
        run.delete()
        return redirect('/workout/')
    
    return render(request, 
                  'workout/run/deleterun.html', 
                  {'run': run})