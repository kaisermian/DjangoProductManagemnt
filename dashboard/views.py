from django.shortcuts import render, redirect
from django.views import View
from dashboard.models import Product

class MainPage(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, "dashboard/home.html", context)


