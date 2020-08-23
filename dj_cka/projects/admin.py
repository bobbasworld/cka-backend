from django.contrib import admin
from projects.models import Project

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author_name', 'published_date',)
    list_display_links = ('title',)
    search_fields = ('id', 'title', 'author_name', 'published_date',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Project, ProjectAdmin)
