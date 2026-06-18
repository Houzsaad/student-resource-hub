from rest_framework import serializers
from .models import Category, Resources,Tag

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'description']
        
        
class ResourcesSerializer(serializers.ModelSerializer):
    #category = serializers.StringRelatedField(read_only=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    category_name = serializers.StringRelatedField(source='category', read_only=True) 
    uploaded_by = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Resources
        fields = "__all__"
        #fields = ['id', 'title', 'description', 'category', 'file', 'uploaded_by', 'tags', 'created_at']
        #read_only_fields = ['uploaded_by', 'created_at']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']