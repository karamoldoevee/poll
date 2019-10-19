from django.contrib import admin
from django.urls import path
from webapp.views.poll_views import IndexView, PollView, PollCreateView, PollUpdateView, PollDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('article/<int:pk>/', PollView.as_view(), name='poll_view'),
    path('article/add/', PollCreateView.as_view(), name='poll_add'),
    path('article/<int:pk>/edit/', PollUpdateView.as_view(), name='poll_update'),
    path('article/<int:pk>/delete/', PollDeleteView.as_view(), name='poll_delete'),
]
