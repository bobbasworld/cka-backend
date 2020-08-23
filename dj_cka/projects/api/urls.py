from django.urls import path, include
from projects.api.views import ProjectListView, ProjectDetailView

urlpatterns = [
    path('', ProjectListView.as_view(), name='project-list'),
    path('<pk>/', ProjectDetailView.as_view(), name='project-detail'),
]
