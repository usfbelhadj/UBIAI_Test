from django.urls import path
from .views import annotate_list
urlpatterns = [
    path('cv/', annotate_list)
]