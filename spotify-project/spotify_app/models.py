from django.db import models


class SongCards(models.Model):
    songTitle = models.TextField()
    songArtist = models.TextField()
    songThumbnail = models.TextField()
    songURL = models.TextField(null=True, blank=True) 
    songCategory = models.CharField(max_length=100, default='Uncategorized')



class SongGenres(models.Model):
    genreName = models.TextField()
    genreThumbnail = models.TextField()
    genreColor = models.CharField(max_length=10, default='#358a6e')


class trendingGenres(models.Model):
    genreName = models.TextField()
    genreThumbnail = models.TextField()