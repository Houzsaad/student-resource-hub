from rest_framework import serializers
from .models import Rating, Comment, Notification

class RatingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Rating
        fields = ['id', 'resource', 'user', 'score', 'created_at']
        #fields = ['__all__']
        read_onLy_fields = ['user', 'created_at']

            

class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'resource', 'user', 'body', 'parent', 'replies', 'created_at']
        read_only_fields = ['created_at']

    def get_replies(self, obj):
        if obj.replies.exists():
            return CommentSerializer(obj.replies.all(), many=True).data
        return []
                                     

class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = ['id', 'message', 'is_read', 'created_at']
        
