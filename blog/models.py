from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

STATUS = ( (0, "Draft"), (1, "Publish") )


class Post(models.Model):
  title = models.CharField(max_length = 255)
  photo_title = models.ImageField(upload_to='images/', blank=True)
  subheading1 = models.CharField(max_length = 255, blank=True)
  body1 = models.TextField(blank=True)
  photo_body1 = models.ImageField(upload_to='images/', blank=True)
  subheading2 = models.CharField(max_length = 255, blank=True)
  body2 = models.TextField(blank=True)
  photo_body2 = models.ImageField(upload_to='images/', blank=True)
  subheading3 = models.CharField(max_length = 255, blank=True)
  body3 = models.TextField(blank=True)
  
  conclusion = models.TextField(blank=True)
  post_links = models.CharField(max_length=255, blank=True)
  slug = models.SlugField(max_length=255, unique=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  status = models.IntegerField(choices=STATUS, default=0)
  
    
  class Meta:
    ordering = ("-created",)

  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
    return reverse("blog:detail", kwargs={"slug":self.slug})

   
    
#marketing de afiliados e publicidade nativa
class TableAffiliate(models.Model):
  category_affiliate = models.CharField(max_length = 200)
  photo_affiliate = models.ImageField(upload_to='images', blank=True)
  name_affiliate = models.TextField()
  website_affiliate = models.TextField()
  commission_affiliate = models.CharField(max_length = 200)
  description_affiliate = models.CharField(max_length = 255)
  author = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name_affiliate



 