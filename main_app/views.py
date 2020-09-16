from django.shortcuts import render
from .models import Record

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>(╯°□°）╯︵ ┻━┻</h1>')

def about(request):
    return render(request, 'about.html')

def records_index(request):
    records = Record.objects.all()
    return render(request, 'records/index.html', { 'records' : records})

def records_detail(request, record_id):
    record = Record.objects.get(id=record_id)
    return render(request, 'records/detail.html', {'record' : record})