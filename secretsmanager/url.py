from django.contrib import admin
from django.urls import path

from secretsmanager.views import homePageView, secretView


urlpatterns = [
    path('', homePageView, name='home'),
    path('secret/', secretView, name='secret')
]
