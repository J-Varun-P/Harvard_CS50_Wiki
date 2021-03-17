from django.urls import path

from . import views



urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("editpage", views.editpage, name="editpage"),
    path("randompage", views.randompage, name="randompage"),
    path("addpage", views.addpage, name="addpage"),
    path("<str:title>", views.title, name="title")
]
