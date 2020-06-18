from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    def __str__(self):
        return self.user.username

class SpNasdaqDmaData(models.Model):
    date = models.DateField('Date')
    sp500 = models.FloatField()
    dma50 = models.FloatField()
class SpNasdaq200DmaData(models.Model):
    date = models.DateField('Date')
    sp500 = models.FloatField()
    dma200 = models.FloatField()