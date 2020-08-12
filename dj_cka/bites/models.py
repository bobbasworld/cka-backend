from django.db import models

# Create your models here.


class Bite(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # published_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(verbose_name='published date')

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
