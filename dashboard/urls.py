from django.urls import path
from dashboard import views

urlpatterns = [
    path('', views.MainPage.as_view(), name='home'),
    path('add/', views.MainPage.as_view(), name="add-product"),
    path('view/<int:pk>/', views.displayProductDetails, name="display-details"),
    path('update/<int:pk>/', views.updateProduct, name='update-product'),
    path('delete/<int:pk>/', views.deleteProduct, name='delete-product'),
]