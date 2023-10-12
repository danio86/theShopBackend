from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Property
from .serializers import PropertySerializer
from django.http import Http404
from the_shop_api.permissions import IsOwnerOrReadOnly

class PropertyList(APIView):
    serializer_class = PropertySerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        properties = Property.objects.all()
        serializer = PropertySerializer(
            properties, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = PropertySerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

class PropertyDetail(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PropertySerializer

    def get_object(self, pk):
        try:
            property = Property.objects.get(pk=pk)
            self.check_object_permissions(self.request, property)
            return property
        except Property.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        property = self.get_object(pk)
        serializer = PropertySerializer(
            property, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        property = self.get_object(pk)
        serializer = PropertySerializer(
            property, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        property = self.get_object(pk)
        property.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
