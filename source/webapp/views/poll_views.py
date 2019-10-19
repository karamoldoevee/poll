from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
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

class PollView(DetailView):
    context_object_name = 'poll'
    template_name = 'poll/poll.html'
    model = Poll

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        poll = self.object
        context['form'] = PollChoiceForm()
        choices = poll.choices.all()
        context['choices'] = choices
        return context
    #

class PollCreateView(CreateView):
    form_class = PollForm
    model = Poll
    template_name = 'poll/create.html'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})

class PollUpdateView(UpdateView):
    model = Poll
    template_name = 'poll/update.html'
    form_class = PollForm
    context_object_name = 'poll'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})

class PollDeleteView(DeleteView):
    model = Poll
    template_name = 'poll/delete.html'
    context_object_name = 'poll'
    success_url = reverse_lazy('index')


