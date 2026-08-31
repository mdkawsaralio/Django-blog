from django.contrib import admin
from assignment.models import About,Sociallink
# Register your models here.

class Aboutadmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count=About.objects.all().count()
        if count==0:
            return True
        else:
            return False



admin.site.register(About,Aboutadmin)
admin.site.register(Sociallink)