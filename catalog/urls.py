from django.urls import path

from catalog.views import (
    index,
    DirectorListView,
    DirectorDetailView,
    ActorListView,
    ActorDetailView,
    MovieListView,
    MovieDetailView,
    MovieCreateView,
)


urlpatterns = [
    path("", index, name="index"),
    path("directors/", DirectorListView.as_view(), name="director-list"),
    path(
        "directors/<int:pk>/",
        DirectorDetailView.as_view(),
        name="director-detail",
    ),
    path("actors/", ActorListView.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetailView.as_view(), name="actor-detail"),
    path("movies/", MovieListView.as_view(), name="movie-list"),
    path("movies/<int:pk>/", MovieDetailView.as_view(), name="movie-detail"),
    path("movies/create/", MovieCreateView.as_view(), name="movie-create"),
]

app_name = "catalog"
