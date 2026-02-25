from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from resume.serializers import EducationSerializer, SkillSerializer, ExperienceSerializer, ExperienceImagesSerializer, SkillImagesSerializer, EducationImagesSerializer
from resume.models import Education, Skill, Experience, ExperienceImages, SkillImages, EducationImages
from rest_framework.exceptions import NotFound
from rest_framework import permissions


class ExperienceViewSet(ModelViewSet): 
    serializer_class = ExperienceSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        user_id = self.request.query_params.get("user_id")
        if user_id:
            return Experience.objects.prefetch_related("images").filter(user_id=user_id).all()
        if self.request.user.is_staff:
            return Experience.objects.prefetch_related("images").all()
        return Experience.objects.none()
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
    
    
class EducationViewSet(ModelViewSet): 
    serializer_class = EducationSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        user_id = self.request.query_params.get("user_id")
        if user_id:
            return Education.objects.prefetch_related("images").filter(user_id=user_id).all()
        if self.request.user.is_staff:
            return Education.objects.prefetch_related("images").all()
        return Education.objects.none()
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    
class SkillViewSet(ModelViewSet): 
    serializer_class = SkillSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        user_id = self.request.query_params.get("user_id")
        if user_id:
            return Skill.objects.prefetch_related("images").filter(user_id=user_id).all()
        if self.request.user.is_staff:
            return Skill.objects.prefetch_related("images").all()
        return Skill.objects.none()
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    

class SkillImagesViewSet(ModelViewSet): 
    serializer_class = SkillImagesSerializer
    def get_queryset(self):
        skill_id = self.kwargs.get("skill_pk")
        if not Skill.objects.filter(id = skill_id).exists(): 
            raise NotFound("Skill does not exist")
        return SkillImages.objects.select_related('skill').filter(skill_id = skill_id)

    def perform_create(self, serializer):
        serializer.save(skill_id=self.kwargs.get("skill_pk"))
    
    
    
class EducationImagesViewSet(ModelViewSet): 
    serializer_class = EducationImagesSerializer
    def get_queryset(self):
        education_id = self.kwargs.get("education_pk")
        if not Education.objects.filter(id = education_id).exists(): 
            raise NotFound("Education does not exist")
        return EducationImages.objects.select_related('education').filter(education_id = education_id)
    
    def perform_create(self, serializer):
        serializer.save(education_id=self.kwargs.get("education_pk"))

    
    
class ExperienceImagesViewSet(ModelViewSet): 
    serializer_class = ExperienceImagesSerializer
    def get_queryset(self):
        experience_id = self.kwargs.get("experience_pk")
        if not Experience.objects.filter(id = experience_id).exists(): 
            raise NotFound("Experience does not exist")
        return ExperienceImages.objects.select_related('experience').filter(experience_id = experience_id)
    
    def perform_create(self, serializer):
        serializer.save(experience_id=self.kwargs.get("experience_pk"))

    
    