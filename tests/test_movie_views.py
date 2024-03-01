from django.test import TestCase
from django.urls import reverse

from catalog.models import Movie, Actor, Director

MOVIE_URL = reverse("catalog:movie-list")


class PublicMovieTests(TestCase):
    def setUp(self) -> None:
        self.movie = Movie.objects.create(
            imdb_id="im1234", title="title", year="2000"
        )
        self.actor = Actor.objects.create(full_name="Actor Name")
        self.director = Director.objects.create(full_name="Director Name")
        self.movie.actors.add(self.actor)
        self.movie.directors.add(self.director)

    def test_movie_list(self) -> None:
        response = self.client.get(MOVIE_URL)
        movies = Movie.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["movie_list"]), list(movies))
        self.assertTemplateUsed(response, "catalog/movie_list.html")

    def test_movie_detail(self) -> None:
        response = self.client.get(
            reverse("catalog:movie-detail", kwargs={"pk": self.movie.pk})
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/movie_detail.html")
        self.assertContains(response, self.movie.title)

    def test_update_movie(self) -> None:
        response = self.client.get(
            reverse("catalog:movie-update", kwargs={"pk": self.movie.pk})
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/movie_form.html")

    def test_create_movie(self) -> None:
        new_data = {
            "title": "Avengers",
            "year": 2020,
            "actors": [self.actor.id],
        }
        response = self.client.post(reverse("catalog:movie-create"), new_data)
        movie = Movie.objects.get(title="Avengers")

        self.assertRedirects(response, MOVIE_URL)
        self.assertEqual(movie.title, new_data["title"])

    def test_movie_list_search(self) -> None:
        Movie.objects.create(
            imdb_id="imdb1234", title="New Movie", year="1984"
        )
        response = self.client.get(MOVIE_URL, {"year": "1984"})

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/movie_list.html")
        self.assertContains(response, "year")
