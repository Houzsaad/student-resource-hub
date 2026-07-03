from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Rating, Comment, Notification
from .serializers import RatingSerializer, CommentSerializer, NotificationSerializer


class RatingCreateView(generics.CreateAPIView):
    serializer_class = RatingSerializer 
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommentListView(generics.ListCreateAPIView):
    # queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    # def get_permissions(self):
    #     if self.action in ['list', 'retrive']:
    #         return [AllowAny()]
    #     else:
    #         return [IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(parent=None)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(owner=self.request.user  )
# Create your views here.
