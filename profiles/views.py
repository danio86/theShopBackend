from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from the_shop_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer
from django.db.models import Count


class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    """
    queryset = Profile.objects.annotate(
        sold_count=Count('owner__property', distinct=True),
        properties_count=Count('owner__property', distinct=True),
        prospective_buyer_count=Count('owner__prospectivebuyer', distinct=True),
        # following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        # 'owner__following__followed__profile',
        # 'owner__followed__owner__profile'
        # 'owner__profile__prospectivebuyers',
        'owner__profile',
    ]
    ordering_fields = [
        'sold_count',
        'owner__sold__created_at',
        'properties_count',
        'prospective_buyer_count',
        # 'following_count',
        # 'owner__following__created_at',
        'owner__prospective_buyer__created_at',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if you're the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
            sold_count=Count('owner__property', distinct=True),
            properties_count=Count('owner__property', distinct=True),
            prospective_buyer_count=Count('owner__prospectivebuyer', distinct=True),
            # following_count=Count('owner__following', distinct=True)
        ).order_by('-created_at')
    serializer_class = ProfileSerializer