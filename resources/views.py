from re import search
from rest_framework import generics, permissions, filters
from .models import Category, Resources, Tag
from .serializers import CategorySerializer, ResourcesSerializer, TagSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import action

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions


import requests
from django.http import HttpResponse

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = []

class ResourcesListCreateView(generics.ListCreateAPIView):
    queryset = Resources.objects.all()
    serializer_class = ResourcesSerializer
    permission_classes = []   

    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']


    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)

class ResourcesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resources.objects.all()
    serializer_class = ResourcesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = []

class ResouceSearchView(generics.ListAPIView):
    queryset = Resources.objects.all()
    serializer_class = ResourcesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
   

class ResourceDownloadView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        try:
            resource = Resources.objects.get(pk=pk)
        except Resources.DoesNotExist:
            return Response({'error': 'Resource not found'}, status=404)

        # Increment counter
        resource.download_count += 1
        resource.save()

        # Fetch file from Cloudinary
        file_url = resource.file.url
        if file_url.startswith('/'):
            # If the file URL is already a full URL, use it directly
            file_url = request.build_absolute_uri(file_url)
    
        response = requests.get(file_url)

        # Serve with download headers
        filename = resource.file.name.split("/")[-1]
        http_response = HttpResponse(
            response.content,
            content_type=response.headers.get('content-type', 'application/octet-stream')
        )
        http_response['Content-Disposition'] = f'attachment; filename="{filename}"'
        return http_response
