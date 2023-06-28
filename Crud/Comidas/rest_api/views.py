from django.shortcuts import render
from .models import Comida, Local
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from .serializers import ComidaSerializer, LocalSerializer
from rest_framework.parsers import JSONParser

# Para autenticación
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@csrf_exempt
@api_view(['GET','POST'])
#@permission_classes((IsAuthenticated,))
def menu_list(request):
    if request.method == 'GET':
        query=Comida.objects.all()
        serializer=ComidaSerializer(query, many=True)
        return Response(serializer.data)
    elif request.method =='POST':
         serializer=ComidaSerializer(data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data,status=status.HTTP_201_CREATED)
         else:
              return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET','POST'])
#@permission_classes((IsAuthenticated,))
def local_list(request):
    if request.method == 'GET':
        query=Local.objects.all()
        serializer=LocalSerializer(query, many=True)
        return Response(serializer.data)
    elif request.method =='POST':
         serializer=LocalSerializer(data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data,status=status.HTTP_201_CREATED)
         else:
              return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
#@permission_classes((IsAuthenticated,))
def menu_detail(request,id):
    try:
        menu=Comida.objects.get(nombre=id)
    except Comida.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer=ComidaSerializer(menu)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = ComidaSerializer(menu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method =='DELETE':
        menu.delete()  
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])
#@permission_classes((IsAuthenticated,))
def local_detail(request,id):
    try:
        lcl=Local.objects.get(nombre=id)
    except Local.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer=LocalSerializer(lcl)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = LocalSerializer(lcl,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method =='DELETE':
        lcl.delete()  
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def login(request):
    data = JSONParser().parse(request)

    username = data['username']
    password = data['password']

    try:
        user = User.objects.get(username = username)
    except User.DoesNotExist:
        return Response("Usuario inválido")
    
    pass_valido = check_password(password, user.password)

    if not pass_valido:
        return("Password incorrecta")
    
    token, created = Token.objects.get_or_create(user=user)

    return Response(token.key)