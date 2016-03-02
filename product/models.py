from __future__ import unicode_literals
from django.db import models

class ProductQuerySet(models.query.QuerySet):
    def nearby(self,latitude,longitude,distance):
        gcd = '6371 * acos(cos(radians(%s)) * cos(radians(latitude))*cos(radians(longitude) - radians(%s)) + sin(radians(%s)) * sin(radians(latitude)))'
        gcd_lt = "{} < %s".format(gcd)
        return self.extra(
                    select={'distance':gcd},
                    select_params=[latitude,longitude,latitude],
                    where=[gcd_lt],
                    params=[latitude,longitude,latitude,distance],
                    order_by=['distance']
                    )

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(model=self.model, using=self._db)

    def nearby(self, latitude, longitude, distance):
        return self.get_queryset().nearby(latitude,longitude,distance)
    
class Product(models.Model):
    title = models.CharField(max_length=20, blank=True, default='')
    mainimage = models.IntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    location = models.CharField(max_length=5)
    latitude = models.FloatField()
    longitude = models.FloatField()
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=10)
    amount = models.IntegerField()
    category = models.ForeignKey('SecondaryCategory', on_delete=models.SET_NULL,null=True)
    postedTime = models.DateTimeField(auto_now_add=True)
    originalPrice = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    brandNew = models.NullBooleanField()
    bargain = models.NullBooleanField()
    exchange = models.NullBooleanField()
    description = models.TextField(blank=True, default='')

    objects = ProductManager()

    def distanceFrom(self,currentGPS):
        lat1, lon1, lat2, lon2 = map(radians, map(float, self.gps.split()+currentGPS.split()))
        dlon = lon2-lon1
        dlat = lat2-lat1
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2*asin(sqrt(a))
        km = 6367*c
        return km

class ImageUUID(models.Model):
	product = models.ForeignKey('Product',on_delete=models.CASCADE,related_name='images')
	uuid = models.CharField(max_length=40)

class Version(models.Model):
    version = models.IntegerField()

class PrimaryCategory(models.Model):
    title = models.CharField(max_length=10)
    icon = models.CharField(max_length=40, blank=True, default='')
    version = models.ForeignKey(Version,default=1)

class SecondaryCategory(models.Model):
    title = models.CharField(max_length=10)
    primaryCategory = models.ForeignKey(PrimaryCategory, related_name='secondary')