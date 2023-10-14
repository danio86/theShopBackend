from rest_framework import generics, permissions
from the_shop_api.permissions import IsOwnerOrReadOnly
from sales.models import Sold
from sales.serializers import SoldSerializer


class SoldList(generics.ListCreateAPIView):
    """
    List sales or create a sold(status) if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SoldSerializer
    queryset = Sold.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SoldDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a sold-status or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = SoldSerializer
    queryset = Sold.objects.all()