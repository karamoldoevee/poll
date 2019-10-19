from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Poll, Choice
from webapp.forms import PollForm, ChoiceForm, PollChoiceForm
from django.core.paginator import Paginator

class IndexView(ListView):
    template_name = 'poll/index.html'
    context_object_name = 'polls'
    model = Poll
    ordering = ['-created_at']
    paginate_by = 5
    paginate_orphans = 1



