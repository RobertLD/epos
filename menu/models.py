from django.db import models    
class Restaurant(models.Model):          
    name = models.CharField(max_length=50)          
    address = models.CharField(max_length=80)          
    phoneNumber = models.CharField(max_length=10)      

    def __str__(self): 
        return "%s the place" % self.name   

class Menu(models.Model):          
    restaurant = models.OneToOneField(Restaurant,on_delete=models.CASCADE,primary_key=True)

class Section(models.Model):
    name = models.CharField(max_length=50)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

class Food(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)