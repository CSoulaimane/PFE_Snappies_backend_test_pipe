from django.urls import path
from snappies import views
urlpatterns = [
    path('getOne/<commande_id>', views.get_commande, name="get_commande"),
    path('getAll', views.get_commandes, name="get_commandes"),

]
