from django.db import models
from cloudinary.models import CloudinaryField
from users.models import User


class Research(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='researches')
    title = models.CharField(max_length=250)
    description = models.TextField()
    link = models.URLField(null=True, blank=True)
    researchers = models.TextField()
    date = models.DateField()
    journal = models.CharField(max_length=200)
    volume_page = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    
    
class ResearchDomain(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='research_domains')
    title = models.CharField(max_length=250)
    description = models.TextField()
    
    def __str__(self):
        return self.title

class Conference(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='conferences')
    title = models.CharField(max_length=200)
    short_title = models.CharField(max_length=100)
    link = models.URLField(null=True, blank=True)
    organizers = models.TextField()
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title
    
    
class ConferenceImages (models.Model):
    conference = models.ForeignKey(
        Conference, on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('conference_image')
    
    
    
class ResearchImages (models.Model):
    research = models.ForeignKey(
        Research, on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('research_image')
    
    

    