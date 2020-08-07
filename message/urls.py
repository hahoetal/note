from django.urls import path
from . import views

urlpatterns = [
    path('userlist/', views.user_list, name="user_list"),
    path('note/<int:receiver_id>', views.create_note, name="create_note"),
    path('notebox_send/', views.send_notes, name="send_notes"),
    path('notebox_received/', views.received_notes, name="received_notes"),
    path('detail/<int:note_id>/', views.detail, name="detail"),
    path('delete_note/<int:note_detail_id>/', views.delete_note, name="delete_note"),
    path('renote/<int:note_detail_id>/', views.renote, name="renote"),
]