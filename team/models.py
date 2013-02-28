from django.db import models
# Create your models here.
   
class Team(models.Model):
    name = models.CharField(unique=False, max_length=50)
    players = models.CharField(unique=False, max_length=50)  

class Players(models.Model):
    number = models.CharField(unique=False, max_length=3)
    name = models.CharField(unique=False, max_length=50)
    position = models.CharField(unique=True, max_length=15)
    height = models.IntegerField(unique=False, null=True, max_length=3)
    weight = models.CharField(unique=False, max_length=3)
    year = models.CharField(unique=False, max_length=5)
    hometown = models.CharField(unique=False, max_length=50)
    school = models.CharField(unique=False, max_length=50)
    #imageurl = models.ImageField(max_length =100)
    
    class Meta(object):
        ordering = ('number', 'name', 'postition', 'height', 'weight', 'year', 'hometown')
    
    def __unicode__(self):
        return U'%s %s' %(self.name, self.pid)
  

    

    