from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from webapp.models import Task


def add_view(request: WSGIRequest):
    if request.method == "GET":
        return render(request, 'task_create.html')
    print(request.POST)
    task_data = {
        'title': request.POST.get('title'),
        'status': request.POST.get('status', 'new'),
        'date': request.POST.get('date', None),
        'description': request.POST.get('description', None)
    }
    task = Task.objects.create(**task_data)
    # return redirect(reverse('task_detail', kwargs={'pk': task.pk}))
    return redirect(f'/')

def detail_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    context = {'task': task}
    return render(request, 'task.html', context=context)

