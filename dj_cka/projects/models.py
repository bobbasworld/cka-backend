from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(verbose_name="published date")
    youtube_embed_url = models.URLField(null=True)

    author_name = models.CharField(max_length=200, null=True, blank=True)
    project_twitter_url = models.URLField(null=True)
    project_twitter_image = models.URLField(null=True)

    def __str__(self):
        return self.title
