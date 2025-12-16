from django.shortcuts import render
from django.shortcuts import get_object_or_404
from polls.models import Film
# Create your views here.
from django.views.generic.detail import DetailView

def index(request):
    context = {}
    return render (request, 'index.html', context)

# def film_detail(request, slug):
#     film = get_object_or_404(Film, slug=slug)
#     return render(request, 'film.html', {'film':film})


class FilmDetailView(DetailView):
    model=Film
    template_name = 'film.html'

    # def get_object(self, queryset = None):
    #     name = self.kwargs.get('name')
    #     return Film.objects.get(name=name)
def films_by_date(request, date):
    print(date, type(date))
    films = Film.objects.filter(created_at__date=date)
    return render(request, 'film.html', {'films': films})

from django.http import HttpResponse

def ip_address(request, ip):
    print(ip, type(ip))
    return HttpResponse(ip)