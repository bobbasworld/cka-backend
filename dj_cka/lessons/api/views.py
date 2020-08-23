from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

from lessons.models import Lesson
from lessons.api.serializers import LessonSerializer


class LessonListView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('id', 'title', 'content', 'level',)


class LessonDetailView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
