from rest_framework import serializers
from .models import Inquiry


class InquirySerializer(serializers.ModelSerializer):
    """
    Serializer for the Inquiry model
    Adds three extra fields when returning a list of Inquiry instances
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Inquiry
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'property', 'created_at', 'updated_at', 'content'
        ]


class InquiryDetailSerializer(InquirySerializer):
    """
    Serializer for the Inquiry model used in Detail view
    Prperty is a read only field so that we dont have to set it on each update
    """
    property = serializers.ReadOnlyField(source='property.id')