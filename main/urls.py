from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('singup', views.singup, name="singup"),
    path('administrator_panel', views.administrator_panel, name="administrator_panel")
]


