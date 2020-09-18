from django.urls import include, path, re_path
from .views import InventoryListView, inventory_content_list, drawing_king_or_club, drawing_black_or_non_face_card

urlpatterns = [
    path('inventory/list/',
         InventoryListView.as_view(), name='inventory_list_view'),
    path('inventory/content/list/',
         inventory_content_list, name='inventory_content_list'),
    path('drawing/king/or/club/',
         drawing_king_or_club, name='drawing_king_or_club'),
    path('drawing/black/or/non/face',
         drawing_black_or_non_face_card, name='drawing_black_or_non_face_card')
]
