from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    # sold_id = serializers.SerializerMethodField()
    properties_count = serializers.ReadOnlyField()
    prospective_buyer_count = serializers.ReadOnlyField()
    sold_count = serializers.ReadOnlyField()
    # following_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
            'content', 'image', 'is_owner', 'properties_count',
            'prospective_buyer_count', 'sold_count'
            # 'following_count'
        ]