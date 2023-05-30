from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from .serializers import EventSerializer
from Events.models import Events

# Create your views here.
@api_view(['POST'])
def createevent(request):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        res = {'msg': 'created successfully'}
        return Response(res)
    else:
         return Response(serializer.errors, status=400)
@api_view(['GET'])
def showevent(request,id=None):
    if id is not None :
        eve=Events.objects.get(id=id)
        serializer=EventSerializer(eve) 
        return Response(serializer.data)
    eve=Events.objects.all()
    serializer=EventSerializer(eve,many=True)
    return Response(serializer.data)
@api_view(['PUT'])
def updateevent(request,id):
    if id is not None :
            eve=Events.objects.get(e_id=id)
            serializer=EventSerializer(eve,data=request.data,partial=True)#model data to python data 
            if serializer.is_valid():
                serializer.save()
                res = {'msg': 'updated succesfully'}
                return Response(res)
            else:
                return Response(serializer.errors, status=400)
@api_view(['DELETE'])
def deleteevent(request,id):
    if id is not None :
            boo=Events.objects.get(e_id=id)
            boo.delete()
            res = {'msg': 'deleted succesfully'}
            return Response(res)
    res = {'msg': 'not able to delete the book !some errror occured'}
    return Response(res, status=400)
        

        

      

