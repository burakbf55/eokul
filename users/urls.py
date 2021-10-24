from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.user_login, name="login"),
    path('register/', views.user_register, name="register"),
    path('logout/', views.user_logout, name="logout"),
    path('note/create/', views.note_create, name="note_create" ),
    path('note_update/<int:pk>', views.note_update, name="note_update" ),
]