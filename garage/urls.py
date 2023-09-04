from django.urls import path
from .views import home, login_view, logout_view, ajouter_voiture,service,site_info_view,carslist,ajouter_employer,staff_list,ajout_testimonial,testimonial_list


urlpatterns = [
    path('admin-home/',home),
    path('connexion/', login_view),
    path('deconnexion/',logout_view),
    path('add-car/', ajouter_voiture),
    path('service',service),
    path('listes-voiture/',carslist),

    path('setting/',site_info_view),
    path('ajouter-employer/',ajouter_employer),
    path('listes-membre',staff_list),
    path('ajouter-temoinage',ajout_testimonial),
    path('listes/',testimonial_list),
]
