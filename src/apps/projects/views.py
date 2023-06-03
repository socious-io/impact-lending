from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, HttpResponse
from .models import Project
from .forms import ProjectForm,  ProjectFormScreen1, ProjectFormScreen2


@login_required
def project_list(request):
    list = Project.objects.all()
    paginator = Paginator(list, 10)

    page_number = request.GET.get('page')
    paginate = paginator.get_page(page_number)

    return render(request, 'projects.html', {'paginate': paginate})


@login_required
def create_project_1(request):
    if request.method == 'POST':
        form = ProjectFormScreen1(request.POST)
        if not form.is_valid():
            return render(request, 'project_screen_1.html', {'form': form}, status=400)

        request.session['project_data'] = {
            'title': form.cleaned_data['title'],
            'subtitle': form.cleaned_data['subtitle'],
            'description': form.cleaned_data['description'],
            'location': form.cleaned_data['location'],
        }

        return redirect('/projects/create/2')

    form = ProjectFormScreen1()
    return render(request, 'project_screen_1.html', {'form': form})


@login_required
def create_project_2(request):
    data = request.session.get('project_data')
    if not data:
        return redirect('/projects/create/1')

    if request.method == 'POST':
        form = ProjectFormScreen2(request.POST)
        if not form.is_valid():
            return render(request, 'project_screen_2.html', {'form': form})

        project = Project(
            user=request.user,
            title=data.get('title'),
            subtitle=data.get('subtitle'),
            description=data.get('description'),
            location=data.get('location'),
            loan_amount=form.cleaned_data['loan_amount'],
            repayment_period=form.cleaned_data['repayment_period']
        )

        project.save()
        request.session['project_data'] = None
        return HttpResponse(project.id)

    form = ProjectFormScreen2()
    return render(request, 'project_screen_2.html', {'form': form})
