from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from catalog.models import Director, Movie, Actor


def index(request: HttpRequest) -> HttpResponse:
    num_movies = Movie.objects.count()
    context = {"num_movies": num_movies}
    return render(request, "catalog/index.html", context=context)


class DirectorListView(generic.ListView):
    model = Director
    # todo: fix N+1


class DirectorDetailView(generic.DetailView):
    model = Director


# class DirectorCreateView(generic.CreateView):
#     model = Director
#     fields = "__all__"
#     success_url = reverse_lazy("catalog:director-list")


# class DirectorUpdateView(LoginRequiredMixin, generic.UpdateView):
#     model = Director
#     fields = "__all__"
#     # template_name = "catalog/genre_form.html"
#     success_url = reverse_lazy("catalog:director-list")
#
#
# class DirectorDeleteView(LoginRequiredMixin, generic.DeleteView):
#     model = Director
#     fields = "__all__"
#     # template_name = "catalog/actor_confirm_delete.html"
#     success_url = reverse_lazy("catalog:director-list")
class ActorListView(generic.ListView):
    model = Actor
    # todo: fix N+1


class ActorDetailView(generic.DetailView):
    model = Actor


class MovieListView(generic.ListView):
    model = Movie
    # todo: fix N+1


class MovieDetailView(generic.DetailView):
    model = Movie
