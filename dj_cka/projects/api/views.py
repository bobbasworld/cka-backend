from rest_framework.generics import ListAPIView, RetrieveAPIView
from projects.api.serializers import ProjectSerializer
from projects.models import Project

from rest_framework.filters import SearchFilter, OrderingFilter


class ProjectListView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = (SearchFilter, OrderingFilter,)
    search_fields = (
        'title', 'content',
        'published_date', 'author_name',
        'project_twitter_url', 'project_twitter_image',
    )


class ProjectDetailView(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
