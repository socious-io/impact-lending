from requests import post
from django.shortcuts import render, HttpResponse

PROOFSPACE_OAUTH = 'https://platform.proofspace.id/oauth/token'
REDIRECT = 'http://localhost:8000/auth/proofspace'


def auth_proofspace(request):
    res = post(PROOFSPACE_OAUTH, params={
        'client_id': '8DXffTYfukQsk3NZZP3ypS',
        'client_secret': 'secretest',
        'code': request.GET.get('code', None),
        'redirect_uri': REDIRECT,
        'grant_type': 'authorization_code'
    })
    print(res)
    return HttpResponse('OK')


def login(request):
    return render(request, 'login.html')


def login_modal(request):
    return render(request, 'login-modal.html')
