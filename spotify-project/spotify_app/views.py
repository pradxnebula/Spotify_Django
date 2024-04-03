from django.shortcuts import render, HttpResponse

from .models import SongCards, SongGenres, trendingGenres



def index(request): 
    genres = SongGenres.objects.all()
    trendingGenre = trendingGenres.objects.all()
    kendrick_lamar = SongCards.objects.filter(songArtist="Kendrick Lamar")
    discover = SongCards.objects.filter(songCategory="Discover")
    rock = SongCards.objects.filter(songCategory="Rock") 
    pop = SongCards.objects.filter(songCategory="Pop")
    jazz = SongCards.objects.filter(songCategory="Jazz")
    indie_india = SongCards.objects.filter(songCategory="Indie India")
    podcasts = SongCards.objects.filter(songCategory="Podcasts")
    travels = SongCards.objects.filter(songCategory="Travels")

    context = {
        'genre_cards': genres,
        'trendGenres': trendingGenre,
        'discover_cards' : discover,
        'indie_india_cards' : indie_india,
        'podcast_cards' : podcasts,
        'travel_cards': travels,
        'rock_cards': rock,
        'kendrick_lamar_cards': kendrick_lamar,
        'pop_cards': pop,
        'jazz_cards': jazz,
    }
    
    return render(request, 'spotify_app/index.html', context)




def about(request): 
    return HttpResponse("about")


def hello(request, first_name):
    return HttpResponse(f"Hello {first_name}")


def add(request, num1, num2):
    return HttpResponse(f"The total sum is {num1+num2}")

