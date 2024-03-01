from django.test import TestCase

from catalog.models import Director, Actor, Movie


class ModelsTests(TestCase):
    def test_director_str(self) -> None:
        director = Director.objects.create(full_name="test")

        self.assertEqual(str(director), director.full_name)

    def test_actor_str(self) -> None:
        actor = Actor.objects.create(full_name="name surname")

        self.assertEqual(str(actor), actor.full_name)

    def test_movie_str(self) -> None:
        movie = Movie.objects.create(
            imdb_id="im1234", title="title", year=2000, plot="best movie ever"
        )
        self.assertEqual(str(movie), f"{movie.title} ({movie.year})")
