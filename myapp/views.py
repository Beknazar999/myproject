from django.contrib.auth.decorators import login_required

@login_required
def my_protected_view(request):

    pass




from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt  
def handle_request(request):
    if request.method == 'GET':
       
        return HttpResponse("Это GET-запрос")

    elif request.method == 'POST':
       
        data = json.loads(request.body.decode('utf-8'))
        response_data = {'message': 'Это POST-запрос', 'received_data': data}
        return JsonResponse(response_data)

    elif request.method == 'PUT':
       
        data = json.loads(request.body.decode('utf-8'))
        response_data = {'message': 'Это PUT-запрос', 'received_data': data}
        return JsonResponse(response_data)

    elif request.method == 'DELETE':
        return HttpResponse("Это DELETE-запрос")

    else:
        return HttpResponse("Метод запроса не поддерживается", status=405)




from myapp.models import Post
from datetime import datetime

post = Post(title='Заголовок', content='Содержание', pub_date=datetime.now())
post.save()



all_posts = Post.objects.all()


post = Post.objects.get(pk=1)
post.title = 'Новый заголовок'
post.save()


post = Post.objects.get(pk=1)
post.delete()


recent_posts = Post.objects.filter(pub_date__gte=datetime.now() - timedelta(days=7))



from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer

class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
    
# views.py

from django.shortcuts import render, get_object_or_404
from .models import YourModel
from .forms import YourModelForm 

def create_view(request):
    # Обработка создания записи
    # ...

def read_view(request, id):
    # Обработка чтения записи
    # ...

def update_view(request, id):
    # Обработка обновления записи
    # ...

def delete_view(request, id):
    # Обработка удаления записи
    # ...

