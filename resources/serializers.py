from rest_framework import serializers
from .models import Category, Resources,Tag, ResourceSubmission

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

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

class ResourceSubmissionSerializer(serializers.ModelSerializer):
    category_name = serializers.StringRelatedField(
        source="category",
        read_only=True
    )

    submitted_by = serializers.StringRelatedField(read_only=True)
    approved_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ResourceSubmission
        fields = [
            "id",
            "resource_type",
            "title",
            "description",
            "file",
            "link",
            "category",
            "category_name",
            "submitted_by",
            "status",
            "approved_by",
            "submitted_at",
            "approved_at",
        ]

        read_only_fields = [
            "submitted_by",
            "status",
            "approved_by",
            "submitted_at",
            "approved_at",
        ]

    def validate(self, attrs):
        resource_type = attrs.get("resource_type")
        file = attrs.get("file")
        link = attrs.get("link")

        if resource_type == "link":
            if not link:
                raise serializers.ValidationError({
                    "link": "A link is required for link resources."
                })

            if file:
                raise serializers.ValidationError({
                    "file": "File is not allowed for link resources."
                })

        if resource_type in ["pdf", "image"]:
            if not file:
                raise serializers.ValidationError({
                    "file": "A file is required for this resource type."
                })

            if link:
                raise serializers.ValidationError({
                    "link": "Link is not allowed for PDF or image resources."
                })

        return attrs