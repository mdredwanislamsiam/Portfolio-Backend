from django.shortcuts import render
from research.models import Research, ResearchDomain, Conference, ConferenceImages, ResearchImages
from research.serializers import ResearchSerializer, ResearchDomainSerializer, ConferenceSerializer, ResearchImagesSerializer, ConferenceImagesSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import NotFound
from rest_framework.filters import OrderingFilter, SearchFilter
from research.paginations import DefaultPagination
from rest_framework import permissions
from django.contrib.auth import get_user_model

User = get_user_model()

class ResearchViewSet(ModelViewSet): 
    serializer_class = ResearchSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = ["title", "journal"]
    ordering_fields = ['date']
    pagination_class = DefaultPagination

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS: 
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
    
    def get_queryset(self):
        user_id = self.request.query_params.get("user_id")
        if user_id: 
            return Research.objects.prefetch_related("images").filter(user_id=user_id).all()
        if self.request.user.is_staff: 
            return Research.objects.prefetch_related("images").all()
        return Research.objects.none()
        
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
    
    
class ResearchDomainViewSet(ModelViewSet): 
    serializer_class = ResearchDomainSerializer
    
    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        user_id = self.request.query_params.get("user_id")
        if user_id:
            return ResearchDomain.objects.filter(user_id=user_id).all()
        if self.request.user.is_staff:
            return ResearchDomain.objects.all()
        return ResearchDomain.objects.none()
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    
class ConferenceViewSet(ModelViewSet): 
    serializer_class = ConferenceSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = ["title", "short_title"]
    ordering_fields = ['date']
    pagination_class = DefaultPagination
    
    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        user_id = self.request.query_params.get("user_id")
        if user_id:
            return Conference.objects.prefetch_related("images").filter(user_id=user_id).all()
        if self.request.user.is_staff:
            return Conference.objects.prefetch_related("images").all()
        return Conference.objects.none()
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    

class ResearchImageViewSet(ModelViewSet): 
    serializer_class = ResearchImagesSerializer
    def get_queryset(self):
        research_id = self.kwargs.get("research_pk")
        if not Research.objects.filter(id = research_id).exists(): 
            raise NotFound("Research does not exist")
        return ResearchImages.objects.select_related('research').filter(research_id = research_id)

    def perform_create(self, serializer):
        serializer.save(research_id=self.kwargs.get("research_pk"))

class ConferenceImageViewSet(ModelViewSet): 
    serializer_class = ConferenceImagesSerializer
    def get_queryset(self):
        conference_id = self.kwargs.get("conference_pk")
        if not Conference.objects.filter(id = conference_id).exists(): 
            raise NotFound("Conference does not exist")
        return ConferenceImages.objects.select_related('conference').filter(conference_id = conference_id)
    
    def perform_create(self, serializer):
        serializer.save(conference_id = self.kwargs.get("conference_pk"))