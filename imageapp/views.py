from imageapp.models import Movie
from django.shortcuts import render
from django.http import Http404

def movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    if Movie is not None:
        return render(request,'movies/movies.html', {'movie':movie})
    else:
        raise Http404('Movie does not exist')
    