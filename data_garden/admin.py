from django.contrib import admin

from data_garden.models import (Location, Site, Project)

class LocationAdmin(admin.ModelAdmin):
    ordering = ('name',)

class SiteAdmin(admin.ModelAdmin):
    ordering = ('name',)

class ProjectAdmin(admin.ModelAdmin):
    ordering = ('name',)

admin.site.register(Location, LocationAdmin)
admin.site.register(Site, SiteAdmin)
admin.site.register(Project, ProjectAdmin)

