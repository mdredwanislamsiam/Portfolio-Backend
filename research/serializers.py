from rest_framework import serializers
from  research.models import Research, ResearchDomain, Conference, ResearchImages, ConferenceImages


class ResearchImagesSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = ResearchImages
        fields = ['id', 'research', 'image']
        read_only_fields = ['research']


class ConferenceImagesSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = ConferenceImages
        fields = ['id', 'conference', 'image']
        read_only_fields = ['conference']


class ResearchSerializer(serializers.ModelSerializer): 
    images = ResearchImagesSerializer(many = True, read_only = True)
    class Meta: 
        model = Research
        fields = ['id', 'user', 'title', 'description', 'link', 'researchers', 'date', 'journal', 'volume_page', 'images']
        read_only_fields = ['user']


class ResearchDomainSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = ResearchDomain
        fields = ['id', 'user', 'title', 'description']
        read_only_fields = ['user']
        
        
class ConferenceSerializer(serializers.ModelSerializer): 
    images = ConferenceImagesSerializer(many = True, read_only = True)
    class Meta: 
        model = Conference
        fields = ['id', 'user', 'title', 'description', 'short_title', 'link', 'organizers', 'date', 'images']
        read_only_fields = ['user']
        
        
        

