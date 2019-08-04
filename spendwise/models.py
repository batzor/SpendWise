from django.db import models
from django.contrib.auth.models import User

class Region(models.Model):
    name = models.CharField(max_length=20)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Tag(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Place(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50)
    keyword = models.CharField(max_length=50)
    tag = models.ForeignKey(Tag, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    description = models.CharField(max_length=50, null=True)
    amount = models.IntegerField()
    place = models.ForeignKey(Place, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.place

    def find_place(self):
        self.place = None
        places = Place.objects.all()
        for place in places:
            if place.keyword == self.description:
                self.place = place
                return
