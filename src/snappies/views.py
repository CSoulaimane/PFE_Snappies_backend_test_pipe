import json
from django.http import HttpResponse
from django.shortcuts import render
from .models import Commande
from django.views.decorators.csrf import csrf_exempt

def get_commande(request, commande_id):
    if request.method == 'GET':
        try:
            commande = Commande.objects.get(id=commande_id)
            commande_data = {'id': commande.id, 'value': commande.value}
            return HttpResponse(json.dumps(commande_data), content_type='application/json')
        except Commande.DoesNotExist:
            return HttpResponse(status=404)


def get_commandes(request):
    if request.method == 'GET':
        commandes = Commande.objects.all()
        commandes_data = [{'id': commande.id, 'value': commande.value} for commande in commandes]
        return HttpResponse(json.dumps(commandes_data), content_type='application/json')
    
@csrf_exempt
def create_commande(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        id = data.get('id')
        value = data.get('value')
        commande = Commande(id=id, value=value)
        commandes_data = {'id': commande.id, 'value': commande.value}

        commande.save()
        return HttpResponse(json.dumps(commandes_data))
    else:
        return HttpResponse('error')
