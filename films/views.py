from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from models import Film,Borough,Genre
from django.template import Context, loader
from django.template import RequestContext
from django.shortcuts import render_to_response
#from mysite1.boroughs.forms import UserForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django import forms
from films.forms import FilmForm

def search_form(request, option):
    borough_list = Borough.objects.all()
    #OrderNotes.objects.filter(item=item).values_list('shared_note', flat=True).distinct()
    zone_list = Borough.objects.values('zone_number').distinct().order_by('zone_number')
    genre_list = Genre.objects.all()
    #if request.GET.get('submit') == 'Search': # change adindaki butonu buldu
        #func_lele()
    if option == "2": #render search page
        return render(request, 'films/searchpage.html', {'zone_list' : zone_list, 'borough_list' : borough_list, 'genre_list' : genre_list})
    elif option == "1":#render search before edit page
        return render(request, 'films/editFilm.html', {'zone_list' : zone_list, 'borough_list' : borough_list, 'genre_list' : genre_list})

def filmOptions(request):
	if request.method == 'GET':
            if request.GET.get("film_but"):
                film_details = Film.objects.get(pk = request.GET.get("film_but"))
                return render(request, 'films/seedetails.html',{'film_details' : film_details})
            elif request.GET.get("film_del_but"):
                f = Film.objects.get(pk=request.GET.get("film_del_but"))
                f.display = 0
                f.save(update_fields=['display'])
                #return HttpResponse("Deleted")
                film_list = Film.objects.filter(rate__gt=4, display=1)
                return render(request,'boroughs/index.html',{'film_list': film_list}) 
            elif request.GET.get("film_update_but"):
                borough_list = Borough.objects.all()
                #OrderNotes.objects.filter(item=item).values_list('shared_note', flat=True).distinct()
                zone_list = Borough.objects.values('zone_number').distinct().order_by('zone_number')
                genre_list = Genre.objects.all()
                f_update = Film.objects.get(pk=request.GET.get("film_update_but"))
                return render(request,'boroughs/filmInfoUpdate.html',{'f_update':f_update, 'zone_list' : zone_list, 'borough_list' : borough_list, 'genre_list' : genre_list})
                #return HttpResponse("Updated")

#add with html form
def film_add(request):
	return render(request, 'films/addFilm.html') 
    
#add via form instance    
def __film_add(request):
    Context = RequestContext(request)
    if request.method == "POST":
        addFilmForm = FilmForm(request.POST)
        if addFilmForm.is_valid():
            film_instance = addFilmForm.save(commit=False)
            film_instance.display = 1
            # film_instance.timestamp = timezone.now() bunun gibi, db de olan ama formda display edilmeyen alanlarin degerleri burda verilebilir.
            film_instance.save()
    else:
        addFilmForm = FilmForm()
        
    return render_to_response(
    		'films/addFilm.html',
    		{'addFilmForm':addFilmForm }, Context)

def film_edit(request):
	pass

def seeFilmDetail(request):
    pass

def searchOptions(request):
    if request.GET.get('SearchBut') == 'Film':
        searchVal = request.GET.get('TextSearchValueF')
        film_objects = Film.objects.filter(film_name__contains=searchVal, display=1)
        #film_objects = Film.objects.get(film_name__iexact = searchVal) #iexact case-insensitive
        
    elif request.GET.get('SearchBut') =='Borough':
        searchVal = request.GET['borough']
        film_objects = Film.objects.filter(film_location=searchVal, display=1)
        
    elif request.GET.get('SearchBut') =='Genre':
        searchVal = request.GET['genre']
        film_objects = Film.objects.filter(film_genre=searchVal, display=1)
        
    elif request.GET.get('SearchBut') =='Zone' :
        searchVal = request.GET['zone']
        #film_objects = Film.objects.select_related('film_location').filter(zone_number=searchVal) 
        film_objects = Film.objects.filter(film_location__zone_number=searchVal, display=1)
        
    elif request.GET.get('SearchBut') == 'Rating' :
        searchVal = request.GET.get('TextSearchValueR')
        film_objects = Film.objects.filter(rate=searchVal, display=1)
        
    return render(request, 'films/searchresult.html', {'film_objects': film_objects})