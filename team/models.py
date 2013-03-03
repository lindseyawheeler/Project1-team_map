from django.db import models
# Create your models here.

class Players(models.Model):
    name = models.CharField(unique=False, max_length=50)
    number = models.CharField(unique=False, max_length=50)
    position = models.CharField(unique=True, max_length=15)
    height = models.IntegerField(unique=False, null=True, max_length=3)
    weight = models.CharField(unique=False, max_length=3)
    year = models.CharField(unique=False, max_length=5)
    hometown = models.CharField(unique=False, max_length=50)
    school = models.CharField(unique=False, max_length=50)
    major = models.CharField(unique=False, max_length=20)
    #imageurl = models.ImageField(max_length =100)
    class Meta(object):
        ordering = ('number', 'name', 'position', 'height', 'weight', 'year',
        'hometown', 'school', 'major',)
    
    def __unicode__(self):
        return U'%s %s' %(self.number, self.name, self.position, self.height,
        self.weight, self.year, self.hometown, self.school, self.major)

   
class Roster(models.Model):
    number = models.CharField(unique=False, max_length=3)
    name = models.CharField(unique=False, max_length=50)
    position = models.CharField(unique=True, max_length=15)
    height = models.IntegerField(unique=False, null=True, max_length=3)
    weight = models.CharField(unique=False, max_length=3)
    year = models.CharField(unique=False, max_length=5)
    hometown = models.CharField(unique=False, max_length=50)
    school = models.CharField(unique=False, max_length=50)
    major = models.CharField(unique=False, max_length=50)
    #imageurl = models.ImageField(max_length =100)
    
    class Meta(object):
        verbose_name_plural = "Rosters"
        ordering = ('number', 'name', 'position', 'height', 'weight', 'year',
        'hometown', 'school', 'major')
    
    def __unicode__(self):
        return U'%s | %s' %(self.number, self.name, self.position, self.height,
        self.weight, self.year, self.hometown, self.school, self.major)
    
    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(Roster, self).save(*args, **kwargs)
    
    
  

    

    