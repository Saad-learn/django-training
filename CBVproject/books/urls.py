from django.urls import path
from .views import ( home_view, book_list_view, book_detail_view, book_create_view, book_update_view, book_delete_view,)
urlpatterns = [
    path("", home_view, name="home"),
    path("books/", book_list_view, name="book_list"),
    path("books/<int:pk>/", book_detail_view, name="book_detail"),
    path("books/add/", book_create_view, name="book_create"),
    path("books/<int:pk>/edit/", book_update_view, name="book_update"),
    path("books/<int:pk>/delete/", book_delete_view, name="book_delete"),
]

