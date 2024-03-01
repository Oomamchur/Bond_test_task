import random

import requests
from django.conf import settings
from django.core.management import BaseCommand

from catalog.models import Director, Actor, Movie


class Command(BaseCommand):
    def scrape_movies(self, quantity: int) -> None:
        count = 0
        while quantity != count:
            imdb_id = "tt" + str(random.randint(0, 9999999)).zfill(8)
            payload = {"apikey": settings.OMDB_API_KEY, "i": imdb_id}
            response = requests.get(
                settings.OMDB_API_URL, params=payload
            ).json()
            if response["Response"] == "True":
                movie, created = Movie.objects.get_or_create(
                    imdb_id=imdb_id,
                    title=response["Title"],
                    year=response["Year"],
                    plot=response["Plot"],
                )
                movie_directors = [
                    Director.objects.get_or_create(full_name=director)[0]
                    for director in response["Director"].split(", ")
                ]
                movie.directors.add(*movie_directors)
                movie_actors = [
                    Actor.objects.get_or_create(full_name=actor)[0]
                    for actor in response["Actors"].split(", ")
                ]
                movie.actors.add(*movie_actors)
                count += 1

    def handle(self, *args, **options):
        self.scrape_movies(30)
