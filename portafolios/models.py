from django.db import models


class Initial(models.Model):
    title= models.CharField(max_length=50, unique=True)
    subtitle= models.CharField(max_length=90, unique=True)
    logo_home= models.ImageField(verbose_name="Your Logo")
    profession= models.CharField(max_length=50)
    who_i_am= models.CharField(verbose_name="Tell something short about you", max_length=1000)
    text_for_backend= models.CharField(max_length=300, verbose_name="backend phrase")
    text_for_front_end= models.CharField(max_length=300, verbose_name="frontend phrase")
    text_for_appsdesktop = models.CharField(max_length=300, verbose_name="apps phrase", unique=True, default='python')
    
    
class Secondary(models.Model):
    photo1= models.ImageField()
    text1= models.TextField()  
    photo2= models.ImageField()
    text2= models.TextField()
    hoto3= models.ImageField() 
    text3= models.TextField()
    
    

class social_media(models.Model):
    email= models.EmailField()
    facebook= models.URLField(verbose_name="Facebook URL User", help_text="Please use your url facebook user page") 
    twitter= models.URLField(verbose_name="Twtter Url User" , help_text="Please use your url twitter user page")
    instagram= models.URLField(verbose_name="Instagram Url User" , help_text="Please use your url Instagram user page")
    

class my_work(models.Model):
    work_photo1= models.ImageField()
    work_text1= models.CharField(max_length=400)
    work_photo2= models.ImageField()
    work_text2= models.CharField(max_length=400)
    work_photo3= models.ImageField()
    work_text3= models.CharField(max_length=400)
    work_photo4= models.ImageField()
    work_text4= models.CharField(max_length=400)


    










# Create your models here.
