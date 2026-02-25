from rest_framework import serializers
from resume.models import Skill, Experience, Education, SkillImages, EducationImages, ExperienceImages


class SkillImagesSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = SkillImages
        fields = ['id', 'skill', 'image']
        read_only_fields = ['skill']


class EducationImagesSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = EducationImages
        fields = ['id', 'education', 'image']
        read_only_fields = ['education']


class ExperienceImagesSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = ExperienceImages
        fields = ['id', 'experience', 'image']
        read_only_fields = ['experience']



class SkillSerializer(serializers.ModelSerializer): 
    images = SkillImagesSerializer(many = True, read_only = True)
    class Meta: 
        model = Skill
        fields = ['id', 'user', 'title', 'description', 'images']
        read_only_fields = ['user']
        

class ExperienceSerializer(serializers.ModelSerializer): 
    images = ExperienceImagesSerializer(many=True, read_only=True)
    class Meta: 
        model = Experience
        fields = ['id', 'user', 'title', 'description', 'start_time',  'end_time', 'images']
        read_only_fields = ['user']
        
        
class EducationSerializer(serializers.ModelSerializer): 
    images = EducationImagesSerializer(many=True, read_only=True)
    class Meta: 
        model = Education
        fields = ['id', 'user', 'degree', 'description', 'start_time',  'end_time', 'institution', 'cgpa', 'images']
        read_only_fields = ['user']

