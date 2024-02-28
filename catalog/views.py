from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from catalog.models import Director, Movie


def index(request: HttpRequest) -> HttpResponse:
    num_movies = Movie.objects.count()
    context = {"num_movies": num_movies}
    return render(request, "catalog/index.html", context=context)


class DirectorListView(generic.ListView):
    model = Director
    queryset = Director.objects.prefetch_related("movies")
    template_name = "catalog/director_list.html"
    context_object_name = "director_list"


class DirectorDetailView(generic.DetailView):
    model = Director


# class DirectorCreateView(LoginRequiredMixin, generic.CreateView):
#     model = Director
#     fields = "__all__"
#     success_url = reverse_lazy("catalog:director-list")
#
#
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
