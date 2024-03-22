from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class ExtendedUser(User):
      user=models.OneToOneField(User,parent_link=True,primary_key=True,on_delete=models.CASCADE)
      phone_no=models.CharField(max_length=12,default=0)  
      alt_no=models.CharField(max_length=12,default=0)
      address=models.CharField(max_length=500,default=0)
      profile_pic=models.ImageField(upload_to='userpics')
      def __str__(self):
            return self.user.username
      
# navbar
class Cateogry(models.Model):
    c_name=models.CharField(max_length=200)
    c1_name=models.CharField(max_length=200)
    c2_name=models.CharField(max_length=200)
    c3_name=models.CharField(max_length=200)
    def __str__(self):
        return self.c_name
    
# Website name
class Title(models.Model):
    t_name = models.CharField(max_length=200)

# front page text
class Content(models.Model):
    a_name = models.CharField(max_length=200)
    b_name = models.CharField(max_length=200)
    c_name = models.CharField(max_length=200)

# headlines of every page
class Headline(models.Model):
    h1_name = models.CharField(max_length=200)
    h2_name = models.CharField(max_length=200)
    h3_name = models.CharField(max_length=200)
    h4_name = models.CharField(max_length=200)
    h5_name = models.CharField(max_length=200)
    h6_name = models.CharField(max_length=200)
    h7_name = models.CharField(max_length=200)

# Website text which use ckeditor
class Webtext(models.Model):
    des=RichTextField()
    des1=RichTextField()
    des2=RichTextField()
    des3=RichTextField()

# four country destination hover
class destination(models.Model):
    a = models.CharField(max_length=200)
    img = models.ImageField(upload_to="image")

# first owl all destination
class alldestinationowl(models.Model):
    a = models.CharField(max_length=200)
    img = models.ImageField(upload_to="image")

# Website images   
class webimage(models.Model):
    image = models.ImageField(upload_to="image")
    bg = models.ImageField(upload_to="image")
    tep = models.ImageField(upload_to="image")
    blog = models.ImageField(upload_to="image")
    explore = models.ImageField(upload_to="image")
    destination = models.ImageField(upload_to="image")
    search = models.ImageField(upload_to="image")
    login = models.ImageField(upload_to="image")


# secound owl latest destination
class latestdesti(models.Model):
    a = models.CharField(max_length=200)
    img = models.ImageField(upload_to="image")

# POPULAR GUIDES books 4
class popularguides(models.Model):
    a = models.CharField(max_length=200)
    img = models.ImageField(upload_to="image")

# website button
class WebButton(models.Model):
    b1_name = models.CharField(max_length=200)
    b2_name = models.CharField(max_length=200)

# Travel Guides
class Travelguides(models.Model):
    a = models.CharField(max_length=200)
    img = models.ImageField(upload_to="image")

# FIND EPIC TOURS & EXPERIENCES
class Experiences(models.Model):
    a = models.CharField(max_length=200)
    img = models.ImageField(upload_to="image")

class Lastpage(models.Model):
    L1_name = models.CharField(max_length=200)
    L2_name = models.CharField(max_length=200)
    L3_name = models.CharField(max_length=200)

class lastpageContent(models.Model):
    l1_name = models.CharField(max_length=200)
    l2_name = models.CharField(max_length=200)
    l3_name = models.CharField(max_length=200)

class blogdesti(models.Model):
    img = models.ImageField(upload_to="image")
    a = models.CharField(max_length=200)
    des=RichTextField()

# ---------about------
class Aboutwho(models.Model):
    img = models.ImageField(upload_to="image")
    a = models.CharField(max_length=200)
    b = models.CharField(max_length=200)
    des=RichTextField()
    des1=RichTextField()