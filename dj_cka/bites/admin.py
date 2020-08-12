from django.contrib import admin
from bites.models import Bite


class BiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'bite_type', 'published_date')
    list_display_links = ('title',)
    search_fields = ('id', 'title', 'bite_type', 'published_date')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


# Register your models here.
admin.site.register(Bite, BiteAdmin)
