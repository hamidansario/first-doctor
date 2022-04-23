"""DiabeticsPredictions URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.Home),
    path("Home.html/", views.Home),
    path("Diabetics/", views.Diabetics),
    path("DiaPredict.html/", views.DiaPredict),
    path("DiaPredict.html/result", views.result),
    path("chatbot.html/", views.chatbot),
    path("Depression.html/", views.Depression),
    path("DepPredict.html/", views.DepPredict),
    path("Heart.html/", views.Heart),
    path("HeaPrediction.html/", views.HeaPrediction),
    path("HeaPrediction.html/outcome", views.outcome)
]
