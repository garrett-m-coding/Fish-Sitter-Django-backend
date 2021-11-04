from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Aquarium
from .serializers import AquariumSerializer
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_aquariums(request):
    aquariums = Aquarium.objects.all()
    serializer = AquariumSerializer(aquariums, many=True)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def user_aquariums(request):
    print('User', f"{request.user.id} {request.user.username} {request.user.zip_code}")
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