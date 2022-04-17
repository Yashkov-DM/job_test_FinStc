from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_db, name='main_db'),
    path('create', views.create, name='create')
]