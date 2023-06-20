from django.conf import settings


def vars(request):
    return {'dapp_env': settings.DAPP_ENV}
