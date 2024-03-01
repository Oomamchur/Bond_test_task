from django.test import TestCase
from django.urls import reverse

from catalog.models import Actor

ACTOR_URL = reverse("catalog:actor-list")


class PublicActorTests(TestCase):
    def setUp(self) -> None:
        self.actor = Actor.objects.create(full_name="name surname")

    def test_actor_list(self) -> None:
        response = self.client.get(ACTOR_URL)
        actors = Actor.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["actor_list"]), list(actors))
        self.assertTemplateUsed(response, "catalog/actor_list.html")

    def test_actor_detail(self) -> None:
        response = self.client.get(
            reverse("catalog:actor-detail", kwargs={"pk": self.actor.pk})
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/actor_detail.html")
        self.assertContains(response, self.actor.full_name)
