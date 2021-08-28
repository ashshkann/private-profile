from django.urls import path
from .views import views_page


urlpatterns = [
    path('', views_page),
]
