from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    path('',views.overview,name='home'),
    path('sysadmin',views.sumbit_ticket,name='sysadmin'),
    path('fetch-ticket/<str:pk>/',views.fetch_ticket,name='fetch-ticket'),
   
   
    path('api/api-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
