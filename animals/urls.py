from django.urls import path
from . import views

urlpatterns = [
    path('animals/', views.AnimalView.as_view()),
    path('animals/<animal_id>', views.AnimalView.as_view())
]