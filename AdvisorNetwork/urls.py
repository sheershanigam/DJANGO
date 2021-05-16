"""AdvisorNetwork URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt import views as jwt_views

from .api import AddAdvisor

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/admin/advisor', csrf_exempt(AddAdvisor.as_view())),
    path('api/user/login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/user/token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('api/user', include('user.urls')),
]
