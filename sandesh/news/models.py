from django.db import models
from django.contrib.auth.models import User
import sqlalchemy as sa


class Newspaper(models.Model):
    newspaper_id = models.AutoField(primary_key=True)
    newspaper_name = models.CharField(max_length=255)
    def __str__(self):
        return self.newspaper_name

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    newspaper = models.ForeignKey(Newspaper, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=255)
    category_url = models.URLField()
    def __str__(self):
        return self.category_name

class News(models.Model):
    news_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    heading = models.CharField(max_length=255)
    news_content = models.TextField()
    # image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    image_url= models.URLField(blank=True, null=True)
    url = models.URLField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.heading[:70]


    
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="profile/",default="default.jpg", blank=True,null=True)

    def __str__(self):
        return self.user.username


# class World(models.Model):
#     title=models.CharField(max_length=300)
#     content=models.TextField()
#     image=models.ImageField(upload_to="post/",blank=True,null=True)
#     date=models.DateField(auto_now_add=True)
#     def __str__(self):
#         return self.title[:70]
    

# class Sports(models.Model):
#     title=models.CharField(max_length=300)
#     content=models.TextField()
#     image=models.ImageField(upload_to="post/",blank=True,null=True)
#     date=models.DateField(auto_now_add=True)
#     def __str__(self):
#         return self.title[:70]
    
# class Trade(models.Model):
#     title=models.CharField(max_length=300)
#     content=models.TextField()
#     image=models.ImageField(upload_to="post/",blank=True,null=True)
#     date=models.DateField(auto_now_add=True)
#     def __str__(self):
#         return self.title[:70]
    