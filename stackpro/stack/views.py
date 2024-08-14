from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import UserSerializer,QuestionSerializer,AnswerSerializer
from .models import Questions,Answers
from rest_framework import authentication,permissions
from rest_framework.decorators import action



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
        
    #     # function to list out question excluding current user's(overriding list funtion)
    # def list(self, request, *args, **kwargs):
    #     queryset = Questions.objects.all().exclude(user=request.user)
    #     serializer = QuestionSerializer(queryset,many=True)
    #     return Response(data=serializer.data)
    
    # OR override built in get_queryset function
    def get_queryset(self):
        return Questions.objects.all().exclude(user=self.request.user)
    
    @action(methods=['POST'],detail=True)
    def add_answer(self,request,*args,**kwargs):
        # get object we want to add answer to
        object = self.get_object()
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user,question=object)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
# create view for answers
        
        

        



