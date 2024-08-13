from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import UserSerializer



# create user creation view using viewsets

class Userview(viewsets.ViewSet):
    def create(self,request,*args,**kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

