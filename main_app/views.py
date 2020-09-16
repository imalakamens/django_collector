from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

class Record:
    def __init__(self, album_title, artist, label, year, size):
        self.album_title = album_title
        self.artist = artist
        self.label = label
        self.year = year
        self.size = size 

records = [
    Record('American Football', 'Americam Football', 'Polyvinyl Record Company', 2014, 12),
    Record('Righteous Fists Of Harmony', 'Daedelus', 'Brainfeeder', 2010, 12),
    Record('Cargo', 'Men At Work', 'Columbia', 1983, 12),
    Record('Locust', 'The Locust', 'Gold Standard Laboratories', 1997, 7),
]

def home(request):
    return HttpResponse('<h1>(╯°□°）╯︵ ┻━┻</h1>')

def about(request):
    return render(request, 'about.html')

def records_index(request):
    return render(request, 'records/index.html', { 'records' : records})