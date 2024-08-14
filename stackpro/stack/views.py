from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import UserSerializer,QuestionSerializer
from .models import Questions,Answers
from rest_framework import authentication,permissions



# create user creation view using viewsets

class Userview(viewsets.ViewSet):
    def create(self,request,*args,**kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        

# Creating view for questions
class QuestionView(viewsets.ModelViewSet):
    serializer_class =QuestionSerializer
    queryset = Questions.objects.all()

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    # since we didnt pass user id we need to override create method
    def create(self, request, *args, **kwargs):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


