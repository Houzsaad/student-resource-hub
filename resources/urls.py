from django.urls import path
from .views import CategoryListCreateView, ResourcesDetailView, ResourcesListCreateView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='categories'),
    path('resources/', ResourcesListCreateView.as_view(), name='resources'),
    path('resources/<int:pk>/', ResourcesDetailView.as_view(), name='resource-detail')
]
