from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Search
from .forms import SearchForm
import folium
import geocoder

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SearchForm()
    
    #address = request.POST.get('address')
    address = Search.objects.all().last()
    
    #location = geocoder.osm('Delhi')

    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country
    if lat == None or lng == None:
        address.delete()
        return HttpResponse('Your input is invalid!')

    #create map object
    m = folium.Map(location=[20, 83], zoom_start=2)
    #folium.Marker([22.445476, 88.390721], tooltip='Click for more', popup='India').add_to(m)
    folium.Marker([lat, lng], tooltip='Click for more', popup=country).add_to(m)


    #get html representations of map object
    m = m._repr_html_()
    context = {
        'm' : m,
        'form' : form,
    }
    return render(request, 'index.html', context)