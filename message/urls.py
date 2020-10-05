from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"), # 첫 페이지
    path('userlist/', views.user_list, name="user_list"), # 쪽지를 보낼 수 있는 사용자 목록
    path('notebox/', views.box, name="box"), # 쪽지함
    path('note/<int:receiver_id>', views.create_note, name="create_note"), # 쪽지 보내기
    path('detail/<int:note_id>/', views.detail, name="detail"),# 쪽지 자세히 보기
    path('delete_note/<int:note_detail_id>/', views.delete_note, name="delete_note"), # 쪽지 삭제하기
    path('renote/<int:note_detail_id>/', views.renote, name="renote"), # 쪽지 답장 보내기
    path('update_note/<int:note_detail_id>/', views.update, name="update_note"), # 쪽지 수정하기
]