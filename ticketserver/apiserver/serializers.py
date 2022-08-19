from rest_framework import serializers
from .models import tickets
from django.contrib.auth.models import User

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['username', 'email', 'password']
        
        
class TicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = tickets
        fields ='__all__'