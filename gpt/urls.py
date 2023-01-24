
from . import views

from django.urls import include, path

urlpatterns = [
    path('', views.index, name='index'),
    path('request/', views.getResponse , name='get-response'),
]