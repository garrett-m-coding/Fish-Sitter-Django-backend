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
        aquarium = Aquarium.objects.filter(id=request.user.id)
        print(aquarium)
        for element in aquarium:
            print(element[{0}])
        # fish = Fish.objects.filter(aquarium_id=aquarium.id)
        # serializer = FishSerializer(fish, many=True)
        return Response(serializer.data)


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