from django.urls import path
from . import views


urlpatterns = [
    path('list', views.project_list),
    path('create/1', views.create_project_1),
    path('create/2', views.create_project_2),
]
