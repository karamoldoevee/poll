from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, \
    UpdateView, DeleteView

from webapp.forms import ChoiceForm, PollChoiceForm
from webapp.models import Poll, Choice

class ChoiceListView(ListView):
    template_name = 'choice/list.html'
    model = Choice
    context_object_name = 'choices'
    paginate_by = 10
    paginate_orphans = 3

class ChoiceForPollCreateView(CreateView):
    model = Choice
    template_name = 'choice/create.html'
    form_class = PollChoiceForm

    def dispatch(self, request, *args, **kwargs):
        self.poll = self.get_poll()
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        self.poll.choices.create(**form.cleaned_data)
        return redirect('poll_view', pk=self.poll.pk)

    def get_poll(self):
        poll_pk = self.kwargs.get('pk')
        return get_object_or_404(Poll, pk=poll_pk)

class ChoiceCreateView(CreateView):
    model = Choice
    template_name = 'choice/create.html'
    form_class = ChoiceForm

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.poll.pk})

class ChoiceUpdateView(UpdateView):
    model = Choice
    template_name = 'choice/update.html'
    form_class = PollChoiceForm
    context_object_name = 'choice'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.poll.pk})

class ChoiceDeleteView(DeleteView):
    model = Choice

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.poll.pk})