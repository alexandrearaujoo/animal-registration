from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from animals.models import Animal

from animals.serializers import AnimalSerializer

# Create your views here.
class AnimalView(APIView):
    def get(self, request):
        animal = Animal.objects.all()

        serializer = AnimalSerializer(animal, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request): 
        serializer = AnimalSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

class AnimalViewDetail(APIView):
    def get(self, request, animal_id):
        animal = get_object_or_404(Animal, pk=animal_id)

        serializer = AnimalSerializer(animal)   

        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request, animal_id):

        animal = get_object_or_404(Animal, pk=animal_id)

        serializer = AnimalSerializer(animal, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        try:
            serializer.save()
        except KeyError as key:
            return Response(
                {"message": f'You can not update {key} property'}, 
                status.HTTP_422_UNPROCESSABLE_ENTITY
            )

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request, animal_id):
        animal = get_object_or_404(Animal, pk=animal_id)

        animal.delete()

        return Response()