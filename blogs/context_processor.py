
from blogs.models import Category
from assignment.models import Sociallink

 

def get_categories(request):
    cateygories=Category.objects.all()
    return dict (categories=cateygories)


def get_social_link(request):
    social_link=Sociallink.objects.all()
    return dict(social_link=social_link)
    