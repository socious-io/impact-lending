# from requests import post
from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import User
from .forms import ProfileForm

PROOFSPACE_OAUTH = 'https://platform.proofspace.id/oauth/token'
REDIRECT = 'http://localhost:8000/auth/proofspace'


def auth_proofspace(request):
    """ res = post(PROOFSPACE_OAUTH, params={
        'client_id': '8DXffTYfukQsk3NZZP3ypS',
        'client_secret': 'secretest',
        'code': request.GET.get('code', None),
        'redirect_uri': REDIRECT,
        'grant_type': 'authorization_code'
    })
    print(res) """
    did = request.GET.get('code', 1234)
    user = User.objects.filter(did=did).first()

    if not user:
        user = User(
            did=did,
            access_token=did,
            refresh_access_token=did
        )
        user.save()
        auth.login(request, user)
        return redirect('/user/update/profile')

    auth.login(request, user)
    return redirect(request.GET.get('next', '/'))


def auth_login(request):
    return render(request, 'login.html')


def auth_login_modal(request):
    return render(request, 'login-modal.html')


@login_required
def update_profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request=request)

        if not form.is_valid():
            return render(request, 'update_profile.html', {'form': form}, status=400)

        user.username = form.cleaned_data['username']
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.country = form.cleaned_data['country']
        user.save()
        return render(request, 'update_profile.html', {'form': form})

    form = ProfileForm(initial={
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'country': user.country
    })

    return render(request, 'update_profile.html', {'form': form})
