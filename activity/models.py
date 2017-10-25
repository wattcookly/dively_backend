from django.db import models


class Activity(models.Model):
    name = models.CharField(max_length=100, verbose_name='Activity', unique=True)
    slug = models.SlugField(max_length=120)
    city = models.ForeignKey('location.City')

    about = models.TextField()

    ordering = models.IntegerField(default=0)
    visible = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
