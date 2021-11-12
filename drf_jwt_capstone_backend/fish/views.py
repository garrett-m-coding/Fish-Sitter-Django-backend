from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Fish
from .models import Aquarium
from .serializers import FishSerializer
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.
# @api_view(['GET'])
# @permission_classes([AllowAny])
# def get_all_fish(request):
#     fish = Fish.objects.all()
#     serializer = FishSerializer(fish, many=True)
#     return Response(serializer.data)


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def aquarium_fish(request):
    if request.method == 'POST':
        serializer = FishSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        #create a variable to capture all aquariums belonging to user
        aquariums = Aquarium.objects.filter(user_id=request.user.id)
        print(aquariums)
        #iterate through user's aquarium objects gathering the aquarium object's ids (aquarium.id)
        aquariums_ids = []
        for e in aquariums:
            append(aquariums_ids)
        #using the single/multiple aquarium.ids search through the fish table and find fish matching these aquarium ids
        #return this list of the users fish objects to user 
 
        # fish = Fish.objects.filter(aquarium_id=aquariums.id)
        # serializer = FishSerializer(fish, many=True)
        # return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def fish_details(request, pk):
    fish = Fish.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = FishSerializer(fish)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = FishSerializer(fish, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        fish.delete()
        return Response({'Alert': 'Fish was successfully deleted.'}, status=status.HTTP_204_NO_CONTENT)