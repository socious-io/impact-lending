from django.contrib import admin
from .models import Project
# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'status', 'user')
    search_fields = ('title', 'subtitle')
    list_filter = ('status', )


admin.site.register(Project, ProjectAdmin)
