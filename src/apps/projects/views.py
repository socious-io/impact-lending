import uuid
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, HttpResponse
from .models import Project, Lend
from .forms import ProjectFormScreen1, ProjectFormScreen2, ProjectFormScreen3


@login_required
def get_project(request, project_id):
    print(project_id)
    project = Project.objects.get(id=project_id)
    return render(request, 'project.html', {'project': project, 'reach_goal_amount': Lend.reach_goal_amount(project)})


@login_required
def project_list(request):
    list = Project.objects.all()
    paginator = Paginator(list, 10)

    page_number = request.GET.get('page')
    paginate = paginator.get_page(page_number)

    return render(request, 'projects.html', {'paginate': paginate})


@login_required
def create_project(request):
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
        return redirect('/projects/create')

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
        request.session['project_id'] = project.id.hex
        return redirect('/projects/create/3')

    form = ProjectFormScreen2()
    return render(request, 'project_screen_2.html', {'form': form})


@login_required
def create_project_3(request):
    id = request.session.get('project_id')
    if not id:
        return redirect('/projects/create/2')

    project = Project.objects.filter(id=id).first()
    if not project:
        return redirect('/projects/create')

    if request.method == 'POST':
        project.status = project.STATUS_FUNDRAISING
        project.save()
        request.session['project_id'] = None
        return HttpResponse('OK')

    return render(request, 'project_screen_3.html', {'project': project})
