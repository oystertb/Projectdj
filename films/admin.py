from django.contrib import admin

from films.models import Borough, Film, Genre

# Register your models here.

class GenreInline(admin.TabularInline):
    model = Genre
    
class BoroughInline(admin.TabularInline):
    model = Borough

class FilmAdmin(admin.ModelAdmin):
    fields = ['film_name','year','rate','director','imdb_link','display','film_location','film_genre']
    #inlines = [ GenreInline, BoroughInline]
        
admin.site.register(Borough)
admin.site.register(Film,FilmAdmin)
admin.site.register(Genre)

# Register your models here.
