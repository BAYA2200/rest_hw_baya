from rest_framework import serializers
from .models import Category, Item


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def validate_name(self, value):
        if "!@#$%^&*" in value:
            raise serializers.ValidationError("You can't use special characters")
        return value


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

    def validate(self, data):
        # if data['category_id'] and data['price'] and data['id'] not in data['qr']:
        #     raise serializers.ValidationError('the necessary data is missing')
        # return data
        if data['category_id'] + data['price'] + data['id'] not in data['qr']:
            raise serializers.ValidationError('the necessary data is missing')
        return data