import json
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, HttpResponse
from .models import Project, Lend
from .forms import ProjectFormScreen1, ProjectFormScreen2


@login_required
def get_project(request, project_id):
    project = Project.objects.get(id=project_id)
    return render(request, 'project_details.html', {'project': project})


@login_required
def project_list(request):
    query = request.GET.get('q')
    list = Project.objects.all()
    if query:
        list = Project.objects.filter(
            Q(title__icontains=query) |
            Q(subtitle__icontains=query) |
            Q(description__icontains=query)
        )

    list.order_by('-created_at')
    paginator = Paginator(list, 10)

    page_number = request.GET.get('page')
    paginate = paginator.get_page(page_number)

    return render(request, 'projects.html', {'paginate': paginate, 'query': query})


@login_required
def create_project(request):

    project = None
    id = request.session.get('project_id')
    if id:
        project = Project.objects.get(id=id)

    if request.method == 'POST':
        form = ProjectFormScreen1(request.POST)
        if not form.is_valid():
            return render(request, 'project_screen_1.html', {'form': form}, status=400)

        if project:
            project.title = form.cleaned_data['title']
            project.subtitle = form.cleaned_data['subtitle']
            project.description = form.cleaned_data['description']
            project.location = form.cleaned_data['location']
            project.save()

        request.session['project_data'] = {
            'title': form.cleaned_data['title'],
            'subtitle': form.cleaned_data['subtitle'],
            'description': form.cleaned_data['description'],
            'location': form.cleaned_data['location'],
        }

        return redirect('/projects/create/2')
    form = ProjectFormScreen1(initial=request.session.get('project_data', {}))
    if project:
        form = ProjectFormScreen1(initial=dict(
            title=project.title,
            subtitle=project.subtitle,
            description=project.description,
            location=project.location
        ))
    return render(request, 'project_screen_1.html', {'form': form})


@login_required
def create_project_2(request):
    data = request.session.get('project_data')
    if not data:
        return redirect('/projects/create')

    project = None
    id = request.session.get('project_id')
    if id:
        project = Project.objects.get(id=id)

    if request.method == 'POST':
        form = ProjectFormScreen2(request.POST)
        if not form.is_valid():
            return render(request, 'project_screen_2.html', {'form': form})

        if project:
            project.loan_amount = form.cleaned_data['loan_amount']
            project.repayment_period = form.cleaned_data['repayment_period']
            project.save()
            return redirect('/projects/create/3')

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
    if project:
        form = ProjectFormScreen2(initial=dict(
                                  loan_amount=project.loan_amount,
                                  repayment_period=project.repayment_period))
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


@login_required
def lending(request, project_id):
    project = Project.objects.get(id=project_id)

    if request.method == 'POST':
        data = json.loads(request.body)
        source = data.get('source')
        tx_hash = data.get('tx_hash')
        amount = data.get('amount')
        try:
            Lend.lending(project, request.user, source, amount, tx_hash)
        except Exception as err:
            return HttpResponse('FAILED', status=400)
        return HttpResponse('OK')

    return render(request, 'lend.html', {'project': project})
