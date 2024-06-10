from django.contrib import admin
from .models import Profile,Newspaper,Category,News
# Register your models here.
admin.site.register(Newspaper)
admin.site.register(Category)
admin.site.register(News)
admin.site.register(Profile)


