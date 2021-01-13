from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
  path('insertDojo', views.insertDojo),
    path('insertNinja', views.insertNinja),

]