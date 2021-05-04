from django.urls import path

from . import views

urlpatterns=[
    path('pypypy/',views.index),  # views..index에  content가 담긴다.
]