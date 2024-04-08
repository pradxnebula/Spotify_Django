from django.contrib import admin

from .models import SongCards, SongGenres, trendingGenres
# Register your models here.

admin.site.register(SongCards);
admin.site.register(SongGenres);
admin.site.register(trendingGenres);
