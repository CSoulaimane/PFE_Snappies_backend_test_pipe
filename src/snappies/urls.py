from django.urls import path
from snappies import views
urlpatterns = [
    path('getOne/<commande_id>', views.get_commande, name="get_commande"),
    path('getAll', views.get_commandes, name="get_commandes"),
    path('create_commande', views.create_commande, name='create_commande'),
    path('helloWorld', views.display_hello_world, name='get_hello_world')
]
