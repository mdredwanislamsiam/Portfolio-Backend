from django.db import models
from users.models import User
from cloudinary.models import CloudinaryField



class Education(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='educations')
    degree= models.CharField(max_length=50)
    start_time = models.DateField()
    end_time = models.DateField(null=True, blank=True)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    institution = models.CharField(max_length=200)
    description = models.TextField(null = True, blank=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.degree}"
    


class Skill (models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skills')
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.user.username} - {self.title}"
    
    

class Experience (models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='experiences')
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateField()
    end_time = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.title}"





class EducationImages (models.Model): 
    education = models.ForeignKey(Education, on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('education_image')
    
    
    
class ExperienceImages (models.Model): 
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('experience_image')
    
    
class SkillImages (models.Model): 
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('skill_image')
    
    
    