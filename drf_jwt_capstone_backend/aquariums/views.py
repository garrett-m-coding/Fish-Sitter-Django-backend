from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Aquarium
from fish.models import Fish
from food.models import Food
from plants.models import Plant
from water_parameters.models import Water_Parameter
from .serializers import AquariumSerializer
from fish.serializers import FishSerializer
from food.serializers import FoodSerializer
from plants.serializers import PlantSerializer
from water_parameters.serializers import Water_ParameterSerializer
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_aquariums(request):
    aquariums = Aquarium.objects.all()
    serializer = AquariumSerializer(aquariums, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_aquarium_relations(request):
	user = request.user
	aquarium = Aquarium.objects.get(user_id=user.id)
	fish = Fish.objects.filter(aquarium=aquarium.id)
	food = Food.objects.filter(aquarium=aquarium.id)
	plants = Plant.objects.filter(aquarium=aquarium.id)
	water_parameters = Water_Parameter.objects.filter(aquarium=aquarium.id)
	aquarium_serializer = AquariumSerializer(aquarium)
	fish_serializer = FishSerializer(fish, many=True)
	food_serializer = FoodSerializer(food, many=True)
	plants_serializer = PlantSerializer(plants, many=True)
	water_parameters_serializer = Water_ParameterSerializer(water_parameters, many=True)
	custom_response_dictionary = {
		'aquarium': aquarium_serializer.data,
		'fish': fish_serializer.data,
		'food': food_serializer.data,
		'plants': plants_serializer.data,
		'water_parameters': water_parameters_serializer.data
	}
	return Response(custom_response_dictionary)



@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def user_aquariums(request):
    print(f"{request.user.first_name} {request.user.last_name} {request.user.username}")
    if request.method == 'POST':
        serializer = AquariumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        aquariums = Aquarium.objects.filter(user_id=request.user.id)
        serializer = AquariumSerializer(aquariums, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def aquarium_details(request, pk):
    aquarium = Aquarium.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = AquariumSerializer(aquarium)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AquariumSerializer(aquarium, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        aquarium.delete()
        return Response({'message': 'Aquarium was successfully deleted.'}, status=status.HTTP_204_NO_CONTENT)