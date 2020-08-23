from django.db import models
from django.conf import settings

from accounts.models import MyUser

# Create your models here.


class Bite(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # published_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(verbose_name='published date')

    author_name = models.CharField(max_length=200, null=True)
    author_description = models.TextField(max_length=200, null=True)
    author_twitter_image = models.URLField(null=True)
    author_twitter_url = models.URLField(null=True)

    FUNDAMENTAL = 'fundamental'
    TECHNICAL = 'technical'
    BITE_TYPE = [
        (FUNDAMENTAL, ('Fundamental')),
        (TECHNICAL, ('Technical')),
    ]

    bite_type = models.CharField(
        max_length=60, choices=BITE_TYPE, default=FUNDAMENTAL, verbose_name="bite type")

    def __str__(self):
        return self.title
