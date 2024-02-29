from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

from catalog.models import Movie, Actor, Director


class MovieForm(forms.ModelForm):
    min_year = 1900
    max_year = 2024
    year = forms.IntegerField(
        required=True,
        validators=[MinValueValidator(min_year), MaxValueValidator(max_year)],
    )
    directors = forms.ModelMultipleChoiceField(
        queryset=Director.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
    )
    actors = forms.ModelMultipleChoiceField(
        queryset=Actor.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Movie
        fields = ("title", "year", "plot", "directors", "actors")


# class MovieSearchForm(forms.Form):
#     title = forms.CharField(
#         max_length=255,
#         required=False,
#         label="",
#         widget=forms.TextInput(
#             attrs={"placeholder": "Search by title or year"}
#         ),
#     )


# class ImdbUserCreationForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#
#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = UserCreationForm.Meta.fields + (
#             "first_name",
#             "last_name",
#             "email"
#         )
