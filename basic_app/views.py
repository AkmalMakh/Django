from django.db import models
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (View, TemplateView, 
                                    ListView, DetailView,
                                    CreateView, UpdateView, 
                                    DeleteView)
from . import models

class IndexView(TemplateView):
    template_name = 'index.html'

class SchoolListView(ListView):
    # defining conetxt object name by default it is school_list because of we are using Listview
    context_object_name = 'schools'
    # returns all the list from school model
    model = models.School

class SchoolDetailView(DetailView):
     # defining conetxt object name by default it is school_list because of we are using Listview
    context_object_name = 'school_details'
    model = models.School
    template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ("name","principal","location")
    model = models.School

class SchooolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School    

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")        