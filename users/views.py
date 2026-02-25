from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from users.serializers import SocialMediaSerializer
from users.models import SocialMedia


class SocialMediaViewSet(ModelViewSet): 
    serializer_class = SocialMediaSerializer
    
    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        user_id = self.request.query_params.get("user_id")
        if user_id:
            return SocialMedia.objects.filter(user_id=user_id).all()
        if self.request.user.is_staff:
            return SocialMedia.objects.all()
        return SocialMedia.objects.none()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
