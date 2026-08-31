
from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Category,Blog
from assignment.models import About,Sociallink



def home (request):
    
    featured_post= Blog.objects.filter(is_featured=True,status='Published').order_by('-updated_at')
    posts=Blog.objects.filter(is_featured=False,status='Published')
    try:
        about=About.objects.get()
    except:
        about=None

    context={
        
        'featured_post':featured_post,
        'posts':posts,
        'about':about,
      }
    
    return render(request,'home.html',context)