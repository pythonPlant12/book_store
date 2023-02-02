from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<slug>", views.book_detailviews, name="book-detail")
]