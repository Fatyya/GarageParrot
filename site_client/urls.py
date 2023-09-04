from django.urls import path
from site_client.views import page_accueil

urlpatterns = [
    path('', page_accueil)
]
