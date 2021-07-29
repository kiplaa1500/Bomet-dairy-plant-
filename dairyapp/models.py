from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from cloudinary.models import CloudinaryField


# Create your models here.
Priority=(
    ('All farmers','All farmers'),
)
servicer=(
    ('Dennis','Dennis'),
    ('Jalody','Jalody'),
    ('Melby','Melby'),
    ('Juma Allan','Juma Allan'),
)
WeeekDays=(
    ('Monday','Monday'),
    ('Tuesday','Tuesday'),
    ('Wednesday','Wednesday'),
    ('Thursday','Thursday'),
    ('Friday','Friday'),
    ('Saturday','Saturday'),
    ('Sunday','Sunday'),
)
class locations(models.Model):
    locations= models.CharField(max_length=100)

    def __str__(self):
        return self.locations

    def save_locations(self):
        self.save()

    @classmethod
    def delete_locations(cls,locations):
        cls.objects.filter(locations=locations).delete()


class Profile(models.Model):
    profpic = CloudinaryField('profile_pics/', blank=True, default = 'image')
    description = HTMLField()
    locations = models.ForeignKey(locations,on_delete=models.CASCADE)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
class Notifications(models.Model):
    title = models.CharField(max_length=100)
    notification = HTMLField()
    priority = models.CharField(max_length=15,choices=Priority,default="CEO")
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    locations = models.ForeignKey(locations,on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
    by=models.CharField(max_length=15,default="Manager")

    def __str__(self):
        return self.title
    

class Dailyrecords(models.Model):
    post_date = models.DateTimeField(auto_now_add=True)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    locations = models.ForeignKey(locations,on_delete=models.CASCADE)
    litres = models.IntegerField(default=0)
    weeekdays=models.CharField(max_length=15,choices=WeeekDays,default="Informational")
    serveBy=models.CharField(max_length=15,choices=servicer,default="Informational")
    
    def __str__(self):
        return self.username.username

class Location(models.Model):
    description = HTMLField()
    locations = models.ForeignKey(locations,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)

    def __str__(self):
        return self.name