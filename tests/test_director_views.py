from django.test import TestCase
from django.urls import reverse

from catalog.models import Director

DIRECTOR_URL = reverse("catalog:director-list")


class PublicDirectorTests(TestCase):
    def setUp(self) -> None:
        self.director = Director.objects.create(full_name="test name")

    def test_director_list(self) -> None:
        response = self.client.get(DIRECTOR_URL)
        directors = Director.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["director_list"]), list(directors)
        )
        self.assertTemplateUsed(response, "catalog/director_list.html")

    def test_director_detail(self) -> None:
        response = self.client.get(
            reverse("catalog:director-detail", kwargs={"pk": self.director.pk})
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/director_detail.html")
        self.assertContains(response, self.director.full_name)
