from django.shortcuts import render

from mywatchlist.models import MyWatchList

# Create your views here.
def show_mywatchlist(request):
    
    data_movie_mywatchlist = MyWatchList.objects.all()
    context = {
        'list_movie': data_movie_mywatchlist,
        'nama': 'Laura'
    }
    
    return render(request, "mywatchlist.html", context)