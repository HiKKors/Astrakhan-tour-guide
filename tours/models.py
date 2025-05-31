from django.db import models
from user.models import CustomUser

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

class Tour(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    cover = models.ImageField(upload_to='covers/')
    created_at = models.DateTimeField(auto_now_add=True)
    avg_rating = models.FloatField(default=0)
    completions = models.PositiveIntegerField(default=0)

class TourPoint(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='points')
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='points/')
    order = models.PositiveIntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()

class Review(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)