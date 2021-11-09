from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Water_Parameter
from .models import Aquarium
from .serializers import Water_ParameterSerializer
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.
@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def aquarium_water_parameters(request):
    if request.method == 'POST':
        serializer = Water_ParameterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # elif request.method == 'GET':
    #     aquarium = Aquarium.objects.filter(id=request.user.id)
    #     print(aquarium)
    #     for element in aquarium:
    #         print(element[{0}])
    #     fish = Fish.objects.filter(aquarium_id=aquarium.id)
    #     serializer = FishSerializer(fish, many=True)
    #     return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def water_parameters_details(request, pk):
    water_parameter = Water_Parameter.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = Water_ParameterSerializer(water_parameter)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = Water_ParameterSerializer(
            water_parameter, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        water_parameter.delete()
        return Response({'Alert': 'Water parameter measurement was successfully deleted.'},
                        status=status.HTTP_204_NO_CONTENT)
