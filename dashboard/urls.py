from django.urls import path
from dashboard import views

urlpatterns = [
    path('', views.MainPage.as_view(), name='home'),
    path('add/', views.MainPage.as_view(), name="add-product"),
    path('update/<int:pk>/', views.updateProductAJAX, name='update-product'),
    path('delete/<int:pk>/', views.deleteProduct, name='delete-product'),
    path('show/<int:pk>/', views.showData, name='show-product'),
]