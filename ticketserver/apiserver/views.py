from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CreateUserSerializer ,TicketsSerializer
from .models import tickets
# authentication import to create user
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
# Create your views here.


@api_view(['GET'])
def overview(request):
    api_urls ={
        'Login':'/login',
        'SignUp':'/signup',
        'authentication':'/api/api-token/',
         }
    return Response(api_urls)


@api_view(['POST'])
def user_signup(request):
    username = request.data['username']
    email = request.data['email']
    password = request.data['password']
    myuser = User.objects.create_user(username,email)
    myuser.set_password(password)
    myuser.save()
    return Response({ "User created": username})


@api_view(['POST'])
def sumbit_ticket(request):
    serializer = TicketsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def fetch_ticket(request,pk):
    result = tickets.objects.filter(user=pk)
    serializer = TicketsSerializer(result, many=True)
    return Response(serializer.data)