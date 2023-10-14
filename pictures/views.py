from rest_framework import generics, permissions
from the_shop_api.permissions import IsOwnerOrReadOnly
from .models import Picture
from .serializers import PictureSerializer, PictureDetailSerializer


class PictureList(generics.ListCreateAPIView):
    """
    List pictures or create a comment if logged in.
    """
    serializer_class = PictureSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Picture.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PictureDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a picture, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PictureDetailSerializer
    queryset = Picture.objects.all()