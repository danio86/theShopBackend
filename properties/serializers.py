from rest_framework import serializers
from properties.models import Property
from sales.models import Sold
from prospectivebuyers.models import Prospectivebuyer
from pictures.models import Picture



class PropertySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    sold_id = serializers.SerializerMethodField()
    prospectivebuyer_id = serializers.SerializerMethodField()
    picture_id = serializers.SerializerMethodField()
    prospectivebuyer_count = serializers.ReadOnlyField()
    inquiries_count = serializers.ReadOnlyField()


    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_sold_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            sold = Sold.objects.filter(
                owner=user, property=obj
            ).first()
            return sold.id if sold else None
        return None

    def get_prospectivebuyer_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            prospectivebuyer = Prospectivebuyer.objects.filter(
                owner=user, property=obj
            ).first()
            return prospectivebuyer.id if prospectivebuyer else None
        return None

    def get_picture_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            picture = Picture.objects.filter(
                owner=user, property=obj
            ).first()
            return picture.id if picture else None
        return None

    class Meta:
        model = Property
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'created_at', 'updated_at', 'title', 'description',
            'price', 'size', 'location', 'num_rooms',
            'sold_date', 'property_type',
            'image', 'image_filter', 'sold_id', 'prospectivebuyer_id',
            'picture_id', 'prospectivebuyer_count',
            'inquiries_count',
            # 'status', 'num_interests'
        ]




    

    

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner