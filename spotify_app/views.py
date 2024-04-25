from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect

from .models import SongCards, SongGenres, trendingGenres


def index(request): 
    songcards = SongCards.objects.all()
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
        'songcards': songcards,
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

def client(request): 
    songcards = SongCards.objects.all()
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
        'songcards': songcards,
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
    
    return render(request, 'spotify_app/client.html', context)



def add(request):
    return render(request,'spotify_app/add.html')

def addSong(request):
   title=request.POST['songTitle']
   artist=request.POST['songArtist']
   thumbnail=request.POST['songThumbnail']
   category=request.POST['songCategory']
   songcards=SongCards(songTitle=title,songArtist=artist,songThumbnail=thumbnail,songCategory=category)
   songcards.save()
   return redirect("/")


def delete(request,id):
    songcards=SongCards.objects.get(id=id)
    songcards.delete()
    return redirect("/")



def update(request,id):
    songcards=SongCards.objects.get(id=id)
    return render(request,'spotify_app/update.html',{'songcards':songcards})

def updateSong(request,id):
    title=request.POST['songTitle']
    artist=request.POST['songArtist']
    thumbnail=request.POST['songThumbnail']
    category=request.POST['songCategory']
    songcards=SongCards.objects.get(id=id)
    songcards.songTitle=title
    songcards.songArtist=artist
    songcards.songThumbnail=thumbnail
    songcards.songCategory=category
    songcards.save()
    return redirect("/")
    
