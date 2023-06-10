from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('login', views.auth_login),
    path('login/modal', views.auth_login_modal),
    path('auth/proofspace', views.auth_proofspace),
]
