from django.db import models

# Create your models here.



class About(models.Model):
    about_heading=models.CharField(max_length= 25)
    about_description=models.TextField(max_length=255)
    updated_at=models.DateTimeField(auto_now=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural="About"
    
    def __str__(self):
        return self.about_heading
    
    
    
class Sociallink(models.Model):
    platform=models.CharField( max_length=50)
    link=models.URLField(max_length=200)
    updated_at=models.DateTimeField(auto_now=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    
    
    def __str__(self):
        return self.platform