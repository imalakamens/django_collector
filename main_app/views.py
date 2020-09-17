from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Record

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def records_index(request):
    records = Record.objects.all()
    return render(request, 'records/index.html', { 'records' : records})

def records_detail(request, record_id):
    record = Record.objects.get(id=record_id)
    return render(request, 'records/detail.html', {'record' : record})

class RecordCreate(CreateView):
    model = Record
    fields = '__all__'