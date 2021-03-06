from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)
    adventure = models.BooleanField(default=False)
    family = models.BooleanField(default=False)
    fantasy = models.BooleanField(default=False)
    comedy = models.BooleanField(default=False)
    thriller = models.BooleanField(default=False)
    romance = models.BooleanField(default=False)
    action = models.BooleanField(default=False)
    horror = models.BooleanField(default=False)
    animation = models.BooleanField(default=False)
    crime = models.BooleanField(default=False)
    drama = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Search(models.Model):
    search = models.CharField(max_length=100)


    def __str__(self):
        return self.search
        
