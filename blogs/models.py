from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    category_name=models.CharField(max_length=50,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural="catagories"


    def __str__(self):
        return self.category_name


status_choice=(
    ('Draft','Draft'),
    ('Published','Published'),
)

class Blog(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField(max_length=150,unique=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="category")
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user")
    featured_image=models.ImageField(upload_to="upload/%y/%m/%d")
    short_description=models.TextField(max_length=500)
    blog_body=models.TextField(max_length=2000)
    status=models.CharField(choices=status_choice,default="Draft",max_length=10)
    is_featured=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title





