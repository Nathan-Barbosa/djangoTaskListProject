from django.shortcuts import render,redirect
from .models import Frame, Task
from .forms import frameForm, taskForm
# Create your views here.
def index(request):
    context = {
        'frames': Frame.objects.all(),
        'tasks': Task.objects.all(),
        'frameForm': frameForm(),
        'taskForm': taskForm()
    }
    if(request.method == 'POST'):
        data = request.POST
        if(len(data) ==3):
            task = taskForm(data)
            if(task.is_valid()):
                addTask = Task(title = data['title'], frame = Frame.objects.get(id=data['frame']))
                addTask.save()
                return redirect('index')
        else:
            frame = frameForm(data)
            if(frame.is_valid()):
                addFrame = Frame(title = data['title'])
                addFrame.save()
                return redirect('index')

    return render(request, 'taskList/index.html', context)

def delete(request):
    id = request.GET['id']
    objectType = request.GET['type']
    if(objectType == 'frame'):
        Frame.objects.filter(id=id).delete()
    elif(objectType == 'task'):
        Task.objects.filter(id=id).delete()
    return redirect('index')