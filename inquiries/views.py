from rest_framework import generics, permissions
from the_shop_api.permissions import IsOwnerOrReadOnly
from .models import Inquiry
from .serializers import InquirySerializer, InquiryDetailSerializer


class InquiryList(generics.ListCreateAPIView):

    """
    List all Inquiries
    Create a new inquiry if authenticated
    Associate the current logged in user with the inquiry
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = InquirySerializer
    queryset = Inquiry.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class InquiryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a inquiry, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = InquiryDetailSerializer
    queryset = Inquiry.objects.all()


