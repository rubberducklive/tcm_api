from django.contrib import admin

from organisations.models import Organisation, Project


@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass
