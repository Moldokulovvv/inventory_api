
from rest_framework import serializers

from main.models import Category, Invent


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class CategoryDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invent
        fields = '__all__'

class InventDetailSerializer(serializers.ModelSerializer):


    class Meta:
        model = Invent
        # fields = ('title', 'serial_number', 'invent_number', 'image', 'description', 'category', 'institution')
        fields = '__all__'


class InventCreateSerializer(serializers.ModelSerializer):


    class Meta:
        model = Invent
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        validated_data['institution'] = user.institution
        invent = Invent.objects.create(**validated_data)
        return invent
