from django.urls import path
from . import views


urlpatterns = [
    path('<uuid:project_id>', views.get_project),
    path('list', views.project_list),
    path('create', views.create_project),
    path('create/2', views.create_project_2),
    path('create/3', views.create_project_3),
]
