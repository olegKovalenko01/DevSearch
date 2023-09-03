from django.shortcuts import render
from .models import Project


def projects(request):
    pr = Project.objects.all()
    print(type(pr))
    context = {'projects': pr}
    return render(request, 'projects/projects.html', context)
