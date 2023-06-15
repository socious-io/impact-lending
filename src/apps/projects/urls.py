from django.urls import path
from . import views


urlpatterns = [
    path('<uuid:project_id>', views.get_project),
    path('<uuid:project_id>/lend', views.lending),
    path('<uuid:project_id>/withdrawn', views.withdrawn),
    path('list', views.project_list),
    path('loans', views.my_loans),
    path('my/list', views.my_projects),
    path('create', views.create_project),
    path('create/2', views.create_project_2),
    path('create/3', views.create_project_3),
]
