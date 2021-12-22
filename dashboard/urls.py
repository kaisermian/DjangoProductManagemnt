from django.urls import path
from dashboard import views

urlpatterns = [
    path('', views.MainPage.as_view(), name='home'),
]