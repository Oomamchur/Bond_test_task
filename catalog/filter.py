from django.db.models import Q
from django_filters import (
    FilterSet,
    CharFilter,
    NumberFilter,
)

from catalog.models import Movie


class MovieFilter(FilterSet):
    title = CharFilter(field_name="title", lookup_expr="icontains", label="Title")
    year = NumberFilter(field_name="year", lookup_expr="exact")
    directors = CharFilter(method="filter_director", label="Director")
    actors = CharFilter(method="filter_actor", label="Actor")

    class Meta:
        model = Movie
        fields = ["title", "year", "directors", "actors"]

    @staticmethod
    def filter_director(queryset, name, value):
        return queryset.filter(
            Q(directors__first_name__icontains=value)
            | Q(directors__last_name__icontains=value)
        )

    @staticmethod
    def filter_actor(queryset, name, value):
        return queryset.filter(
            Q(actors__first_name__icontains=value)
            | Q(actors__last_name__icontains=value)
        )
