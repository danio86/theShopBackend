from rest_framework import generics, permissions
from the_shop_api.permissions import IsOwnerOrReadOnly
from prospectivebuyers.models import Prospectivebuyer
from prospectivebuyers.serializers import ProspectivebuyerSerializer


class ProspectivebuyerList(generics.ListCreateAPIView):
    """
    List prospectivebuyers or create a prospectivebuyer if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ProspectivebuyerSerializer
    queryset = Prospectivebuyer.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProspectivebuyerDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a prospectivebuyer or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProspectivebuyerSerializer
    queryset = Prospectivebuyer.objects.all()