from django.urls import path
from .views import handle_request

urlpatterns = [
    path('handle_request/', handle_request, name='handle_request'),
]




from django.urls import path
from .views import ItemListCreateView, ItemDetailView

urlpatterns = [
    path('items/', ItemListCreateView.as_view(), name='item-list-create'),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
]




from django.urls import path
from .views import create_view, read_view, update_view, delete_view

urlpatterns = [
    path('create/', create_view, name='create'),
    path('<int:id>/', read_view, name='read'),
    path('<int:id>/update/', update_view, name='update'),
    path('<int:id>/delete/', delete_view, name='delete'),
]
