from rest_framework import generics, permissions, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import redirect


from .models import Category, Resources, Tag
from .serializers import (
    CategorySerializer,
    ResourcesSerializer,
    TagSerializer,
)


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = []


class ResourcesListCreateView(generics.ListCreateAPIView):
    queryset = Resources.objects.all()
    serializer_class = ResourcesSerializer
    permission_classes = []

    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "description"]

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.uploaded_by == request.user
    
class ResourcesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resources.objects.all()
    serializer_class = ResourcesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = []

    
class ResouceSearchView(generics.ListAPIView):
    queryset = Resources.objects.all()
    serializer_class = ResourcesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ResourceDownloadView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        try:
            resource = Resources.objects.get(pk=pk)
        except Resources.DoesNotExist:
            return Response(
                {"error": "Resource not found"},
                status=404
            )

        # Increment download count
        resource.download_count += 1
        resource.save(update_fields=["download_count"])

        # Redirect directly to Cloudinary
        return redirect(resource.file.url)