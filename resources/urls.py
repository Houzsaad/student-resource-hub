from django.urls import path
from .views import CategoryListCreateView, ResourcesDetailView, ResourcesListCreateView, TagListCreateView, ResourceSearchView, ResourceDownloadView, ResourceSubmissionListCreateView, PendingResourceSubmissionListView, ApproveResourceSubmissionView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='categories'),
    path('resources/', ResourcesListCreateView.as_view(), name='resources'),
    path('resources/<int:pk>/', ResourcesDetailView.as_view(), name='resource-detail'),
    path('tags/', TagListCreateView.as_view(), name='tags'),
    path('search/', ResourceSearchView.as_view(), name='search'),
    path('resources/<int:pk>/download/', ResourceDownloadView.as_view(), name='resource-download'),


    path('submissions/', ResourceSubmissionListCreateView.as_view(), name='resource-submissions'),
    path('submissions/pending/', PendingResourceSubmissionListView.as_view(), name='pending-resource-submissions'),
    path('submissions/<int:pk>/approve/', ApproveResourceSubmissionView.as_view(), name="approve-resource-submission"),
]