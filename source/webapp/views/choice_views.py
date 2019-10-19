from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, \
    UpdateView, DeleteView

from webapp.forms import ChoiceForm, PollChoiceForm
from webapp.models import Poll, Choice

class ChoiceListView(ListView):
    template_name = 'comment/list.html'
    model = Choice
    context_object_name = 'choices'
    paginate_by = 10
    paginate_orphans = 3

