from django.urls import path, include
from .views import LessonListView, LessonDetailView

urlpatterns = [
    path('', LessonListView.as_view()),
    path('<pk>', LessonDetailView.as_view()),
]
