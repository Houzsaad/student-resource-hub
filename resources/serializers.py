from rest_framework import serializers
from .models import Category, Resources

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'description']
        
        
class ResourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resources
        fields = ['id', 'title', 'description', 'category', 'file', 'uploaded_by', 'created_at']
        read_only_fields = ['created_at']

        # def create(self, validated_data):
        #     validated_data['uploaded_by'] = self.context['request'].user
        #     return super().create(validated_data)