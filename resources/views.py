from re import search
from rest_framework import generics, permissions, filters
from .models import Category, Resources, Tag
from .serializers import CategorySerializer, ResourcesSerializer, TagSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import action

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions



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
    permission_classes = []

class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = []

class ResouceSearchView(generics.ListAPIView):
    queryset = Resources.objects.all()
    serializer_class = ResourcesSerializer
    permission_classes = []
   

    # def get_queryset(self):
    #     return Resources.objects.all()
    

class ResourceDownloadView(APIView):
    permission_classes = []

    def get(self, request, pk):
        try:
            resource = Resources.objects.get(pk=pk)
        except Resources.DoesNotExist:
            return Response({'error': 'Resource not found!'}, status=404)
        
        resource.download_count += 1
        resource.save()

        return Response({
            'title': resource.title,
            'file_url': request.build_absolute_uri(resource.file.url),
            'download_count': resource.download_count
        })

# Create your views here.
