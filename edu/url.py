from django.urls import  path

from . import views

urlpatterns = [
    path('alumnis/',views.alumni,name='alumnis'),
]