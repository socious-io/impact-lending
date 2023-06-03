from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from src.apps.users.models import User

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
        return redirect('/users/update/profile')

    auth.login(request, user)
    return redirect(request.GET.get('next', '/'))


def auth_login(request):
    return render(request, 'login.html')


def auth_login_modal(request):
    return render(request, 'login-modal.html')


@login_required
def index(request):
    return render(request, 'index.html')


def connect(request):
    return render(request, 'connect.html')
