from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    #path("pyhton", views.pyhton_course, name="pyhton"),
    #path("java", views.java_course, name="java")
    path("<str:item>", views.course, name="course"),
    path("<int:num1>/<int:num2>", views.multiply_view, name="multi"),
]

