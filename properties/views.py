from rest_framework import generics, permissions
from the_shop_api.permissions import IsOwnerOrReadOnly
from .models import Property
from .serializers import PropertySerializer


class PropertyList(generics.ListCreateAPIView):
    """
    List properties or create a post if logged in
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Property.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PropertyDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a property and edit or delete it if you own it.
    """
    serializer_class = PropertySerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Property.objects.all()