from re import search

from rest_framework import generics, permissions, filters
from .models import Category, Resources, Tag
from .serializers import CategorySerializer, ResourcesSerializer, TagSerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

class ResourcesListCreateView(generics.ListCreateAPIView):
    queryset = Resources.objects.all()
    serializer_class = ResourcesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perfom_creation(self, serializer):
        serializer.save(uploaded_by=self.request.user)

class ResourcesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resources.objects.all()
    serializer_class = ResourcesSerializer
    permission_classes = [permissions.IsAuthenticated]

class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]

class ResouceSearchView(generics.ListAPIView):
    serializer_class = ResourcesSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_field = ['title', 'description', 'tas__name', 'category__name']

    def get_queryset(self):
        return Resources.objects.all()
    


# Create your views here.
