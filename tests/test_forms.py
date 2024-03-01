from django.test import TestCase
from django.urls import reverse

from catalog.forms import MovieForm
from catalog.models import Actor, Director, Movie


class FormsTest(TestCase):
    def setUp(self) -> None:
        self.actor = Actor.objects.create(full_name="Actor Name")
        self.director = Director.objects.create(full_name="Director Name")

    def test_movie_creation_form_is_valid(self) -> None:
        form_data = {
            "title": "Title",
            "year": 2000,
            "actors": [self.actor.id],
            "directors": [self.director.id],
        }
        form = MovieForm(data=form_data)
        is_valid = form.is_valid()
        self.client.post(reverse("catalog:movie-create"), data=form_data)
        new_movie = Movie.objects.get(title=form_data["title"])

        self.assertTrue(is_valid)
        self.assertEqual(new_movie.title, form_data["title"])

    def test_movie_creation_form_is_not_valid(self) -> None:
        form_data = {"title": "Title", "year": 1800}
        form = MovieForm(data=form_data)

        self.assertFalse(form.is_valid())
