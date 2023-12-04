import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
from snappies.models import User

@csrf_exempt
def user_create(request):
    if request.method == 'POST':
        # Lire les données JSON de la requête
        data = json.loads(request.body)
        value = data.get('value')
      
        user = User.objects.create(
                value=value,
            )
        return JsonResponse({'success': 'User created', 'user': user.id})
       
    else:
        return JsonResponse({'error': 'Invalid request method'})



def user_read_all(request):
    if request.method == 'GET':
        # Récupérer tous les objets User de la base de données
        users = User.objects.all()
        # Créer une liste de dictionnaires avec les attributs des utilisateurs
        users_list = []
        for user in users:
            users_list.append({
                "id": user.id,
                "value": user.value,
                
            })
        # Renvoyer la liste des utilisateurs au format JSON
        return JsonResponse({"users": users_list})
    else:
        return JsonResponse({"error": "Invalid request method"})