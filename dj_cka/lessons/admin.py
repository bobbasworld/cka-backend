from django.contrib import admin
from .models import Lesson


class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'level',)
    search_fields = ('level', 'title',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


# Register your models here.
admin.site.register(Lesson, LessonAdmin)
