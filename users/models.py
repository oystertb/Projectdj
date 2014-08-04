from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    #istedigimiz ek ozellikler
    website = models.URLField(blank=True)
    #home address phone num
    #picture = models.ImageField(upload_to='user_images', blank=True)
    
    def __unicode__(self):
        return self.user.username
