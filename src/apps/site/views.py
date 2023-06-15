import requests
from django.conf import settings
from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from src.apps.users.models import User


def auth_proofspace(request):
    code = request.GET.get('code', None)
    res = requests.post(settings.PROOFSPACE_AUTH_URL, params={
        'client_id': settings.PROOFSPACE_AUTH_CLIENT_ID,
        'client_secret': settings.PROOFSPACE_AUTH_CLIENT_SECRET,
        'code': code,
        'redirect_uri': settings.PROOFSPACE_AUTH_REDIRECT_URL,
        'grant_type': 'authorization_code'
    })
    print(res, '----------------------------')
    user = User.objects.filter(did=code).first()

    if not user:
        user = User(
            did=code,
            access_token=code,
            refresh_access_token=code
        )
        user.save()
        auth.login(request, user)
        return redirect('/users/profile/update')

    auth.login(request, user)
    return redirect(request.GET.get('next', '/'))


def auth_login(request):
    return render(request, 'login.html')


def auth_login_modal(request):
    return render(request, 'login-modal.html', {
        'proofspace_client_id': settings.PROOFSPACE_AUTH_CLIENT_ID,
        'proofspace_redirect_url': settings.PROOFSPACE_AUTH_REDIRECT_URL
    })


@login_required
def index(request):
    return redirect('/projects/list')
