from django.conf import settings
from time import time


def vars(request):
    return {
        'dapp_env': settings.DAPP_ENV,
        'time': int(time())

    }
