from django.urls import path 
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("<int:num1>/", views.course_number_view, name = "course_number_view"),
    path("<str:item>/", views.course, name = "course"), #Input Alma İşlemi
    path("<int:num1>/<int:num2>/", views.multiply_view, name = "multiply"),
]