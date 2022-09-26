from rest_framework import serializers
from .models import tickets,guide
from django.contrib.auth.models import User

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['username', 'email', 'password']
        
        
class TicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = tickets
        fields ='__all__'
        
        
class GuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = guide
        fields ='__all__'