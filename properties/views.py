from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Property
from .serializers import PropertySerializer


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

    def property(self, request):
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