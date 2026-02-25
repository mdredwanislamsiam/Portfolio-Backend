from research.views import ResearchDomainViewSet, ResearchViewSet, ConferenceViewSet, ResearchImageViewSet, ConferenceImageViewSet
from resume.views import EducationViewSet, EducationImagesViewSet, SkillViewSet, SkillImagesViewSet, ExperienceViewSet, ExperienceImagesViewSet
from rest_framework_nested import routers
from django.urls import path, include


router = routers.DefaultRouter()
router.register('researches', ResearchViewSet, basename='researches')
router.register('research_domains', ResearchDomainViewSet, basename='research_domains')
router.register('conferences', ConferenceViewSet, basename='conferences')
router.register('skills', SkillViewSet, basename='skills')
router.register('educations', EducationViewSet, basename='education')
router.register('experiences', ExperienceViewSet, basename='experiences')


research_router = routers.NestedDefaultRouter(router, 'researches', lookup = 'research')
research_router.register('images', ResearchImageViewSet, basename='research-images')


conference_router = routers.NestedDefaultRouter(router, 'conferences', lookup ='conference')
conference_router.register('images', ConferenceImageViewSet, basename='conference-images')


skill_router = routers.NestedDefaultRouter(router, 'skills', lookup='skill')
skill_router.register('images', SkillImagesViewSet, basename='skill-images')


experience_router = routers.NestedDefaultRouter(router, 'experiences', lookup='experience')
experience_router.register('images', ExperienceImagesViewSet, basename='experience-images')


education_router = routers.NestedDefaultRouter(router, 'educations', lookup = 'education')
education_router.register('images', EducationImagesViewSet, basename='education-images')


urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
] + router.urls + research_router.urls + conference_router.urls + skill_router.urls + experience_router.urls + education_router.urls
