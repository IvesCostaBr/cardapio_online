from django.urls import path
from .views import IndexView, PetiscosView



urlpatterns = [
    path('', IndexView.as_view()),
    path('petiscos/', PetiscosView.as_view())
]
