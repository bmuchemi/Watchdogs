from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Neighbourhood(models.Model):
    hood = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    pi = models.ImageField(upload_to='images/')
    description = models.TextField()
    hospital_num = models.IntegerField(null=True, blank=True)
    police_num = models.IntegerField(null=True, blank=True)
    occupant_count = models.IntegerField(null=True, blank=True)
    admin = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
            return ( self.hood)
    def create_neighbourhood(self):
        self.save()
    
    def delete_neighbourhood(self):
        self.delete()

    def search_by_hood(search_term):
        hood=Neighbourhood.objects.filter(hood__icontains=search_term)
        return hood


class Profile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    pic = models.ImageField(upload_to='images/' ,default='images/default.jpg',null=True)
    bio = models.TextField( default="Please Update Bio")
    id_number = models.IntegerField(default = 0, unique = True)
    hood=models.ForeignKey(Neighbourhood, on_delete=models.CASCADE,null=True)
    number = models.IntegerField(default =0)
    email = models.EmailField(default = "Enter your valid email address", unique =True)

    def __str__(self):
        return '{} {}'.format(self.pic.url, self.bio)


    def save_profile(self):
        self.save()
        
class Buisness(models.Model):
   name = models.CharField(max_length = 100)
   owner = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
   hood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE,null=True)
   image = models.ImageField(upload_to='images/')
   description = models.TextField()
   email = models.EmailField(default = "Please input buisness email address")

   def create_buisness(self):
        self.save()
    
   def delete_buisness(self):
        self.delete()

   def search_by_name(search_term):
        bizna=Buisness.objects.filter(name__icontains=search_term)
        return bizna

class Post(models.Model):
    title = models.CharField(max_length=100, null=True)
    post = models.TextField()
    image = models.ImageField(upload_to='images/')
    date = models.DateTimeField(auto_now_add=True)
    owner = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    hood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} Post'

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

