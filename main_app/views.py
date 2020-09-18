from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Record, Crate
from .forms import ReviewForm

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
    orphan_crates = Crate.objects.exclude(id__in = record.crate_set.all().values_list('id'))
    review_form = ReviewForm()
    return render(request, 'records/detail.html', {
        'record' : record, 'review_form' : review_form, 'crates': orphan_crates
        })

class RecordCreate(CreateView):
    model = Record
    fields = '__all__'

class RecordUpdate(UpdateView):
    model = Record
    fields = ['artist','label','year','size']

class RecordDelete(DeleteView):
    model = Record
    success_url = '/records/'

def add_review(request, record_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.record_id = record_id
        new_review.save()
    return redirect('detail', record_id=record_id)

class CrateList(ListView):
    model = Crate
    
class CrateDetail(DetailView):
    model = Crate

class CrateCreate(CreateView):
    model = Crate
    fields = ['owner']

class CrateUpdate(UpdateView):
    model = Crate
    fields = ['owner']

class CrateDelete(DeleteView):
    model = Crate
    success_url = '/crates/'

def assoc_crate(request, record_id, crate_id):
    Crate.objects.get(id=crate_id).records.add(record_id)
    return redirect('detail', record_id=record_id)