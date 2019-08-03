"""bourse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from marketview import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('panel/', views.panel, name='panel'),
    path('api/v1/getDailyData/<str:InsCode>', views.getDailyData, name='getDailyData'),
    path('api/v1/getShareholders/<str:InsCode>', views.getShareHolders, name='getShareHolders'),
    path('api/v1/getOHLC/<str:InsCode>', views.getOHLC, name='getOHLC'),
    path('api/v1/getSymbols', views.getSearchSymbols, name='getSearchSymbols'),
    path('api/v1/getLastAnalysis/<int:Count>', views.getLastAnalysis, name='getLastAnalysis'),
    path('api/v1/auth/obtain_token', obtain_jwt_token, name='ObtainJWTToken'),
    path('api/v1/auth/refresh_token', refresh_jwt_token, name='RefreshJWTToken'),    
]
