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
    path('signup',views.user_signup,name='signup'),
    path('email',views.get_users,name='signup'),    
    path('guide',views.guide_link,name='guide'),
     path('guide_url',views.guide_url,name='guide_url'),
    
    path('api/api-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
