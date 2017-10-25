from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100, verbose_name='Country', unique=True)
    slug = models.SlugField(max_length=120)
    ordering = models.IntegerField(default=0)
    visible = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100, verbose_name='City', unique=True)
    slug = models.SlugField(max_length=120)
    country = models.ForeignKey(Country)
    ordering = models.IntegerField(default=0)
    visible = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
