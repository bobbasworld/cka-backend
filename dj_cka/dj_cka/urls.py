"""dj_cka URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# customize admin site
admin.site.site_header = 'CKA Admin'
admin.site.site_title = 'CKA Admin'
admin.site.index_title = 'CKA Administration'

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('admin/', admin.site.urls),
    path('api/lessons/', include('lessons.api.urls')),
    path('api/bites/', include('bites.api.urls')),
    path('api/projects/', include('projects.api.urls')),
]
