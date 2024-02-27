from django.db import models


class Director(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        ordering = ("last_name",)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        ordering = ("last_name",)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Movie(models.Model):
    title = models.CharField(max_length=255, unique=True)
    year = models.IntegerField()
    description = models.TextField(blank=True)
    directors = models.ManyToManyField(Director, related_name="movies")
    actors = models.ManyToManyField(Actor, blank=True, related_name="movies")

    class Meta:
        ordering = ("year",)

    def __str__(self) -> str:
        return f"{self.title} ({self.year})"
