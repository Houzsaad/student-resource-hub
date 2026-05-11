from django.urls import path
from .views import RatingCreateView, CommentListView, NotificationListView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('ratings/', RatingCreateView.as_view(), name='ratings'),
    path('comments/', CommentListView.as_view(), name='comments'),
    path('notifications/', NotificationListView.as_view(), name='notifications'),
]
