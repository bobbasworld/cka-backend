from rest_framework.generics import ListAPIView, RetrieveAPIView
from bites.api.serializers import BiteSerializer
from bites.models import Bite

from rest_framework.filters import SearchFilter, OrderingFilter


class BiteListView(ListAPIView):
    queryset = Bite.objects.all()
    serializer_class = BiteSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = (
        'title', 'content',
        'published_date', 'bite_type',
        'author_name', 'author_twitter_image',
        'author_twitter_url',
    )


class BiteDetailView(RetrieveAPIView):
    queryset = Bite.objects.all()
    serializer_class = BiteSerializer
