from django.urls import path
from . import views

app_name= 'youtube'
urlpatterns = [
    path('', views.index, name='index'),
    path('genre/<int:pk>/', views.genre, name='genre'),
    path('notables/<int:pk>/', views.notables, name='notables'),
    path('notables/<int:pk>/<int:notableIndex>', views.notablesDetail, name='notablesDetail'),
    path('link/<int:pk>', views.link, name='link'),
]