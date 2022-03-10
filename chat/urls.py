from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    #path('', views.login, name='login'),
    path('chat/', views.index, name='index'),
    path('chat/<str:room_name>/', views.room, name='room'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
