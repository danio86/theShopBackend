from rest_framework import serializers
from django.db import IntegrityError
from prospectivebuyers.models import Prospectivebuyer


class ProspectivebuyerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Prospectivebuyer model
    The create method handles the unique constraint on 'owner' and 'property'
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Prospectivebuyer
        fields = ['id', 'created_at', 'owner', 'property']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })