from django.urls import path, include
from bites.api.views import BiteListView, BiteDetailView

urlpatterns = [
    path('', BiteListView.as_view()),
    path('<pk>/', BiteDetailView.as_view()),
]
