from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ask-for-event/', views.ask_for_event, name='ask_for_event'),
]