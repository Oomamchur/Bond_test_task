from django.db import models


class Director(models.Model):
    full_name = models.CharField(max_length=255)

    class Meta:
        ordering = ("full_name",)

    def __str__(self) -> str:
        return f"{self.full_name}"


class Actor(models.Model):
    full_name = models.CharField(max_length=255)

    class Meta:
        ordering = ("full_name",)

    def __str__(self) -> str:
        return f"{self.full_name}"


class Movie(models.Model):
    imdb_id = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    plot = models.TextField(blank=True)
    directors = models.ManyToManyField(
        Director, blank=True, related_name="movies"
    )
    actors = models.ManyToManyField(Actor, blank=True, related_name="movies")

    class Meta:
        ordering = ("year",)

    def __str__(self) -> str:
        return f"{self.title} ({self.year})"
