from django.urls import path
from . import views

urlpatterns = [
    path('', views.guess_the_player, name='guess_the_player'),
]
