from django.views.generic import TemplateView, DeleteView, UpdateView, CreateView, ListView, DetailView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import BookForm
from .models import Book

class HomeView(TemplateView):
    template_name = "books/base.html"

class BookListView(ListView):
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "books"

    def get(self, request, *args, **kwargs):
        messages.info(request, "Book list loaded successfully.")
        return super().get(request, *args, **kwargs)

class BookDetailView(DetailView):
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "book"

    def get(self, request, *args, **kwargs):
        messages.info(request, "Book Detail View.")
        return super().get(request, *args, **kwargs)

@method_decorator(login_required, name="dispatch")
class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = "books/book_form.html"
    success_url = reverse_lazy("book_list")

    def get(self, request, *args, **kwargs):
        messages.info(request, "Book Created Successfully.")
        return super().get(request, *args, **kwargs)

@method_decorator(login_required, name="dispatch")
class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = "books/book_form.html"
    success_url = reverse_lazy("book_list")

    def get(self, request, *args, **kwargs):
        messages.info(request, "Book Updated Successfully.")
        return super().get(request, *args, **kwargs)


@method_decorator(login_required, name = "dispatch")
class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = "books/book_confirm_delete.html"
    success_url = reverse_lazy("book_list")

    def get(self, request, *args, **kwargs):
        messages.info(request, "Book Deleted")
        return super().get(request, *args, **kwargs)