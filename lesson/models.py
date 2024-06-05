from django.db import models

class Genre(models.Model):
    name_of_genre = models.CharField(max_length=100)

    def __str__(self):
        return self.name_of_genre

class Game(models.Model):
    game_name = models.CharField(max_length=100)
    name_of_genre = models.ManyToManyField(Genre)
    year = models.IntegerField()
    rating = models.FloatField()

    def __str__(self):
        return self.game_name