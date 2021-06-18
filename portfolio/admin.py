from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('ceated', 'updated')

#admin.site.register(Project,ProjectAdmin)

admin.site.register(Project)

