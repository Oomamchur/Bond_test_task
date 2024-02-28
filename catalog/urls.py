from django.urls import path

from catalog.views import index, DirectorListView

urlpatterns = [
    path("", index, name="index"),
    path("directors/", DirectorListView.as_view(), name="director-list"),
    # path("directors/<int:pk>/", DirectorDetailView.as_view(), name="actor-detail"),
    # path("directors/create/", DirectorCreateView.as_view(), name="actor-create"),
    # path("directors/<int:pk>/update/",
    #      DirectorUpdateView.as_view(),
    #      name="actor-update"
    #      ),
    # path("directors/<int:pk>/delete/",
    #      DirectorDeleteView.as_view(),
    #      name="actor-delete"
    #      ),
]

app_name = "catalog"
