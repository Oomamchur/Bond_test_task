from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from catalog.filter import MovieFilter
from catalog.forms import MovieForm
from catalog.models import Director, Movie, Actor


def index(request: HttpRequest) -> HttpResponse:
    num_movies = Movie.objects.count()
    queryset = Movie.objects.order_by("-id")[:3]
    context = {"num_movies": num_movies, "movie_list": queryset}
    return render(request, "catalog/index.html", context=context)


class DirectorListView(generic.ListView):
    model = Director
    queryset = Director.objects.prefetch_related("movies")
    paginate_by = 25


class DirectorDetailView(generic.DetailView):
    model = Director


class ActorListView(generic.ListView):
    model = Actor
    queryset = Actor.objects.prefetch_related("movies")
    paginate_by = 25


class ActorDetailView(generic.DetailView):
    model = Actor


class MovieListView(generic.ListView):
    model = Movie
    paginate_by = 25

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filterset = None

    def get_queryset(self):
        queryset = Movie.objects.prefetch_related("actors", "directors")
        self.filterset = MovieFilter(self.request.GET, queryset=queryset)

        return self.filterset.qs

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(MovieListView, self).get_context_data(**kwargs)
        context["search_form"] = self.filterset.form

        return context


class MovieDetailView(generic.DetailView):
    model = Movie


class MovieCreateView(generic.CreateView):
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy("catalog:movie-list")


class MovieUpdateView(generic.UpdateView):
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy("catalog:movie-list")


class MovieDeleteView(generic.DeleteView):
    model = Movie
    template_name = "catalog/movie_confirm_delete.html"
    success_url = reverse_lazy("catalog:movie-list")
