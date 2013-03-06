from django.db import models
# Create your models here.

class Players(models.Model):
    name = models.CharField(unique=True, max_length=50)
    number = models.CharField(unique=True, max_length=50)
    position = models.CharField(unique =False, max_length=15)
    height = models.CharField(unique=False, null=True, max_length=3)
    weight = models.CharField(unique=False, max_length=3)
    year = models.CharField(unique=False, max_length=5)
    hometown = models.CharField(unique=False, max_length=50)
    school = models.CharField(unique=False, max_length=50)
    major = models.CharField(unique=False, max_length=20)
    img = models.CharField(max_length =100)
    
    class Meta(object):
        ordering = ('number', 'name', 'position', 'height', 'weight', 'year',
        'hometown', 'school', 'major',)
    
    def __unicode__(self):
        return U'%s %s' %(self.number, self.name, self.position, self.height,
        self.weight, self.year, self.hometown, self.school, self.major)

   
class Roster(models.Model):
    name = models.CharField(unique=True, max_length=50)
    coach = models.CharField(unique=True, max_length=50)
    wins = models.CharField(unique=True, max_length=15)
    losses = models.CharField(unique=False, null=True, max_length=3)
    home_wins = models.CharField(unique=False, max_length=3)
    home_losses = models.CharField(unique=False, max_length=5)
    away_wins = models.CharField(unique=False, max_length=50)
    away_losses = models.CharField(unique=False, max_length=50)
    players = models.ManyToManyField(Players)
  
    
    class Meta(object):
        verbose_name_plural = "Rosters"
        ordering = ('name', 'coach', 'wins', 'losses', 'home_wins',
                    'home_losses', 'away_wins', 'away_losses' )
    
    def __unicode__(self):
        return U'%s | %s' %(self.name, self.coach)
   
  

    

    