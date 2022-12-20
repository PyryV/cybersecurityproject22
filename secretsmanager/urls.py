from django.contrib import admin
from django.urls import path

from secretsmanager.views import logoutView, addSecret, homePageView, loginView, secretView, newSecretView


urlpatterns = [
    path('', homePageView, name='home'),
    path('secret/<int:id>', secretView, name='secret'),
    path('new/', newSecretView, name='newSecret'),
    path('addnew/', addSecret, name='addSecret'),
    path('login/', loginView, name='login'),
    path('logout/', logoutView, name='logout')
]
