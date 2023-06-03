from django.shortcuts import render
from .forms import ProjectForm,  ProjectFormScreen1, ProjectFormScreen2


def create_project_screen_1(request):

    form = ProjectFormScreen1()
    return render(request, 'project_screen_1.html', {'form': form})


def create_project_screen_2(request):

    form = ProjectFormScreen2()
    return render(request, 'project_screen_2.html', {'form': form})
