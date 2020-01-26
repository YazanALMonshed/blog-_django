from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_data, name="home-page"),
    path('contact/', views.show_info, name="contact-page"),
]
