from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('problem/', views.problem, name='problem'),
    path('solution/', views.solution, name='solution'),
    path('how-it-works/', views.how_it_works, name='how_it_works'),
    path('register/', views.register_page, name='register'),
]
