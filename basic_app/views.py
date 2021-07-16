from django.db import models
from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
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

