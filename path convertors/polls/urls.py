from django.urls import path, register_converter
from . import views, converters

register_converter(converters.DateConverter, "date")
register_converter(converters.IPv4convertor, "ipv4")
urlpatterns = [
    path('', views.index, name = 'index'),
    path('films/<slug:slug>/', views.FilmDetailView.as_view(), name = 'film-detail')
    path('films/date/<date:date>/', views.films_by_date, name = 'films_by_date')
    path('ips/<ipv4:ip>/', views.ip_address, name = 'ip-address'),
]