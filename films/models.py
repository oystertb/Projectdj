from django.db import models

# Create your models here.
class Borough(models.Model):
    borough_name = models.CharField(max_length=200)
    zone_number = models.IntegerField()
    
    def __unicode__(self):
        return self.borough_name
        
class Genre(models.Model):
    genre_name = models.CharField(max_length = 200)
    
    def __unicode__(self):
        return self.genre_name
        
class Film(models.Model):
    film_name = models.CharField(max_length=200)
    year = models.IntegerField()
    rate = models.IntegerField()
    director = models.CharField(max_length=200)
    imdb_link = models.CharField(max_length=200)
    display = models.IntegerField()
    film_location = models.ForeignKey(Borough)
    film_genre = models.ManyToManyField(Genre) # kendisi intersection table yaratiyor.
    
    def __unicode__(self):
        return self.film_name