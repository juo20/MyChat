"""mychat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from account.views import (
    registration_view,
    login_request,
    logout_request,
)

from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('MyChat/', include('chat.urls'), name="start"),
    path('MyChat/chat/', include('chat.urls'), name="home"),
    path('admin/', admin.site.urls),
    path('register/', registration_view, name="register"),
    path('login/', login_request, name="login"),
    path('logout/', logout_request, name="logout"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
