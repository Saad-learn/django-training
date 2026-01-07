from django.shortcuts import render, HttpResponse
from .models import Author, Contact, Article

# Create your views here.
def index(request):
    author = Author.objects.get(id=1)
    article1 = Article.objects.create(title="article 1", content="description", author=author)
    articl2 = Article.objects.create(title="article 2", content="description", author=author)
    articles_by_author = author.articles.all()
    article = Article.objects.get(id=1)
    return HttpResponse(author.name, articl2, article1, articles_by_author)
    