from django.shortcuts import render
from django.http import Http404


from .models import task
from .serializers import ListSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status    


class adminlist(APIView):
    
    def get(self , request):
        lists = task.objects.all()
        serializer = ListSerializer(lists , many=True)
        return Response(serializer.data)
    
    def post(self , request):
        serializer = ListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response("your data is invalid",status=status.HTTP_400_BAD_REQUEST)
        
        
class detaillist(APIView):
    def get_object(self, pk ):
        try :
            list = task.objects.get(pk=pk)
        except task.DoesNotExist :
            raise Http404
        return list     
    def get(self , request,pk):
        list = self.get_object(pk)
        serializer = ListSerializer(list)
        return Response(serializer.data)
    
    def put(self , request,pk):
        list = self.get_object(pk)
        serializer = ListSerializer(list,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response("your data is invalid",status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        list =self.get_object(pk)
        list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


