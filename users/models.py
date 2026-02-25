from django.db import models
from django.contrib.auth.models import AbstractUser 
from cloudinary.models import CloudinaryField



class User(AbstractUser): 
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    bio = models.TextField(null = True, blank=True)
    profile_image = CloudinaryField('profile_image', null = True, blank = True)
    cover_image = CloudinaryField('cover_image', null= True, blank = True)
    
    def __str__(self):
        return self.username
    
    
class SocialMedia(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='socials')
    site_name = models.CharField(max_length=200)
    link = models.URLField()
    icon = CloudinaryField('icon')
    