from django.db import models
from django.contrib.auth.models import User

class Region(models.Model):
    name = models.CharField(max_length=20)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

class Tag(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    keyword = models.CharField(max_length=50)

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    description = models.CharField(max_length=50, null=True)
    amount = models.IntegerField()
    tag = models.ForeignKey(Tag, null=True, on_delete=models.SET_NULL)

    def assign_tag(self):
        self.tag = None
        tags = Tag.objects.all()
        for tag in tags:
            if tag.keyword in self.description:
                self.tag = tag
                return
