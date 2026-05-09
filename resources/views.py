from rest_framework import generics, permissions
from .models import Category, Resources
from .serializers import CategorySerializer, ResourcesSerializer

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


# Create your views here.
