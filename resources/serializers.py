from rest_framework import serializers
from .models import Category, Resources,Tag

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'description']
        
        
# class ResourcesSerializer(serializers.ModelSerializer):
    
#     category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
#     category_name = serializers.StringRelatedField(source='category', read_only=True) 
#     uploaded_by = serializers.StringRelatedField(read_only=True)
#     class Meta:
#         model = Resources
#         fields = "__all__"

class ResourcesSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    category_name = serializers.StringRelatedField(source='category', read_only=True)
    uploaded_by = serializers.StringRelatedField(read_only=True)
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Resources
        fields = "__all__"

    def get_is_owner(self, obj):
        request = self.context.get('request')
        return bool(request and request.user.is_authenticated and obj.uploaded_by == request.user)

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']