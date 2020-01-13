from django.db import models

class restaurant(models.Model):
    phone_number = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    rating_reviews = models.IntegerField()
    rating_average = models.FloatField()
    name = models.CharField(max_length=200)
    photos_url = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    reviews_url = models.CharField(max_length=200)
    longitude = models.FloatField()
    slug = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=200)
    profile_image_url = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    latitude = models.FloatField()
    restaurant_id = models.IntegerField()
    description = models.CharField(max_length=200)