from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from the_shop_api.permissions import IsOwnerOrReadOnly
from .models import Property
from .serializers import PropertySerializer


class PropertyList(generics.ListCreateAPIView):
    """
    List properties or create a property if logged in
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Property.objects.annotate(
        prospectivebuyer_count=Count('prospectivebuyers', distinct=True),
        inquiries_count=Count('inquiry', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    # seachbar choose from fields
    search_fields = [
        'owner__username',
        'title',
        'location',
        'price',
        'size',
    ]
    ordering_fields = [
        'prospectivebuyer_count',
        'inquiries_count',
        'prospectivebuyer_count__created_at',
        'inquiries_count__created_at',
    ]
    filterset_fields = [
        'prospectivebuyers__owner__profile', 
        'owner__profile',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PropertyDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a property and edit or delete it if you own it.
    """
    serializer_class = PropertySerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Property.objects.annotate(
        prospectivebuyer_count=Count('prospectivebuyers', distinct=True),
        inquiries_count=Count('inquiry', distinct=True)
    ).order_by('-created_at')