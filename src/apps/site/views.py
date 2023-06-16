import base64
import json
import requests
from django.conf import settings
from django.contrib import auth
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from src.apps.users.models import User


def auth_proofspace(request):
    code = request.GET.get('code', None)
    res = requests.post(settings.PROOFSPACE_AUTH_URL, data={
        'client_id': settings.PROOFSPACE_AUTH_CLIENT_ID,
        'client_secret': settings.PROOFSPACE_AUTH_CLIENT_SECRET,
        'code': code,
        'redirect_uri': settings.PROOFSPACE_AUTH_REDIRECT_URL,
        'grant_type': 'authorization_code'
    })

    if res.status_code > 300:
        return HttpResponse(res.text, status=res.status_code)

    response = res.json()

    payloads = response['access_token'].split('.')
    payload_data = decode_base64(payloads[1])
    payload_json = json.loads(payload_data)
    did = payload_json['connectDid']

    user = User.objects.filter(did=did).first()

    if not user:
        user = User(
            did=did,
            access_token=response['access_token'],
            refresh_access_token=response['refresh_token']
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


def decode_base64(base64_message):
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.urlsafe_b64decode(base64_bytes + b'===')
    message = message_bytes.decode('ascii')
    return message
