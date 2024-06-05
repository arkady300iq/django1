import django_setup
from lesson.models import Genre, Game


'''need = Game.objects.get(id=3)
need.delete()
'''

genre1 = Genre(
    name_of_genre = "Horror"
).save()

genre2 = Genre(
    name_of_genre = "Strategy"
).save()

genre3 = Genre(
    name_of_genre = "Simulation"
).save()

genre4 = Genre(
    name_of_genre = "Shooter"
).save()



game1 = Game(
    game_name='CS:GO', 
    year=1999, 
    rating=9.5)
game1.save()
game1.name_of_genre.add(genre4)

game2 = Game(
    game_name='Age of Empires II', 
    year=1990, 
    rating=7.5)
game2.save()
game2.name_of_genre.add(genre2)

game3 = Game(
    game_name='The Sims', 
    year=2000, 
    rating=8.5)
game3.save()
game3.name_of_genre.add(genre4)

game4 = Game(
    game_name='Resident Evil', 
    year=1996, 
    rating=8.5)
game4.save()
game4.name_of_genre.add(genre4)

