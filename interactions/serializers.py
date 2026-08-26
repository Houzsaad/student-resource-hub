from rest_framework import serializers
from .models import Rating, Comment, Notification

# class RatingSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Rating
#         fields = ['id', 'resource', 'user', 'score', 'created_at']
#         read_only_fields = ['user', 'created_at']        

class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ['id', 'resource', 'user', 'score', 'created_at']

        read_only_fields = ['user', 'created_at']

        #fields = ['__all__']
        read_only_fields = ['user', 'created_at']


    def validate_resource(self, value):
        request = self.context.get('request')

        if request and request.user.is_authenticated:
            already_rated = Rating.objects.filter(
                resource=value,
                user=request.user
            ).exists()

            if already_rated:
                raise serializers.ValidationError ("You have already rated this resource.")
        return value

        #             "You've already rated this resource."
        #         )
        # return value
            

class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'

    def get_replies(self, obj):
        if obj.replies.exists():
            return CommentSerializer(obj.replies.all(), many=True).data
        return []
                                     

class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = ['id', 'message', 'is_read', 'created_at']
        
