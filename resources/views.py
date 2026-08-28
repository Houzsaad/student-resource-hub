from rest_framework import generics, permissions, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import redirect
from django.utils import timezone

from .models import Category, Resources, Tag, ResourceSubmission
from .serializers import (
    CategorySerializer,
    ResourcesSerializer,
    TagSerializer,

    ResourceSubmissionSerializer
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


class MyResourcesView(generics.ListAPIView):
    serializer_class = ResourcesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Resources.objects.filter(
            uploaded_by=self.request.user
        ).order_by("-created_at")


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.uploaded_by == request.user


class CanApproveResource(permissions.BasePermission):
    message = "You do not have permission to approve resources."

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.has_perm("resources.can_approve_resource")

        )
    

class ResourceApprovalPermissionView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response({
            "can_approve_resource": request.user.has_perm(
                "resources.can_approve_resource"
            )
        })

    
class PendingResourceSubmissionListView(generics.ListAPIView):
    serializer_class = ResourceSubmissionSerializer
    permission_classes = [CanApproveResource]

    def get_queryset(self):

        return ResourceSubmission.objects.filter(
            status=ResourceSubmission.Status.PENDING
        )
    
class ApproveResourceSubmissionView(generics.UpdateAPIView):
    queryset = ResourceSubmission.objects.all()
    serializer_class = ResourceSubmissionSerializer
    permission_classes = [CanApproveResource]

    def post(self, request, pk):
        try:
            submission = ResourceSubmission.objects.get(pk=pk)
        except ResourceSubmission.DoesNotExist:
            return Response(
                {"error": "Submission not found"},
                status=404
            )

        if submission.status != ResourceSubmission.Status.PENDING:
            return Response(
                {"error": "This submission has already been processed."},
                status=400
            )

        resource = Resources.objects.create(
            resource_type=submission.resource_type,
            title=submission.title,
            description=submission.description,
            file=submission.file,
            link=submission.link,
            category=submission.category,
            uploaded_by=submission.submitted_by,
        )

        submission.status = ResourceSubmission.Status.APPROVED
        submission.approved_by = request.user
        submission.approved_at = timezone.now()
        submission.save()

        return Response({
            "message": "Resource approved successfully.",
            "resource_id": resource.id,
            "submission_id": submission.id,
        })

class RejectResourceSubmissionView(APIView):
    permission_classes = [CanApproveResource]

    def post(self, request, pk):
        try:
            submission = ResourceSubmission.objects.get(pk=pk)
        except ResourceSubmission.DoesNotExist:
            return Response(
                {"error": "Submission not found"},
                status=404
            )

        if submission.status != ResourceSubmission.Status.PENDING:
            return Response(
                {"error": "This submission has already been processed."},
                status=400
            )

        submission.status = ResourceSubmission.Status.REJECTED
        submission.approved_by = request.user
        submission.approved_at = timezone.now()
        submission.save()

        return Response({
            "message": "Resource submission rejected successfully.",
            "submission_id": submission.id,
            "status": submission.status,
        })

        
    
class ResourcesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resources.objects.all()
    serializer_class = ResourcesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = []

    
class ResourceSearchView(generics.ListAPIView):
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

class ResourceSubmissionListCreateView(generics.ListCreateAPIView):
    queryset = ResourceSubmission.objects.all()
    serializer_class = ResourceSubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(submitted_by=self.request.user)


