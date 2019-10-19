from django.contrib import admin
from django.urls import path
from webapp.views.poll_views import IndexView, PollView, PollCreateView, PollUpdateView, PollDeleteView
from webapp.views.choice_views import ChoiceListView, ChoiceCreateView, ChoiceForPollCreateView, ChoiceUpdateView, ChoiceDeleteView
# from  webapp.views.views import AnswerView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('poll/<int:pk>/', PollView.as_view(), name='poll_view'),
    path('poll/add/', PollCreateView.as_view(), name='poll_add'),
    path('poll/<int:pk>/edit/', PollUpdateView.as_view(), name='poll_update'),
    path('poll/<int:pk>/delete/', PollDeleteView.as_view(), name='poll_delete'),
    path('choice/add/', ChoiceCreateView.as_view(), name='choice_add'),
    path('choice/<int:pk>/edit/', ChoiceUpdateView.as_view(), name='choice_update'),
    path('choice/<int:pk>/delete/', ChoiceDeleteView.as_view(), name='choice_delete'),
    path('choice/<int:pk>/add-choice/', ChoiceForPollCreateView.as_view(), name='poll_choice_create'),
]
