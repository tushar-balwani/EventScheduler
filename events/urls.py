from django.urls import path
from .views import EventCreateView, EventUpdateView, EventDeleteView, EventListView, EventDetailsView

urlpatterns = [
    path('', EventCreateView.as_view(), name='create_event'),
    path('', EventListView.as_view(), name='list_event'),
    path('<int:pk>/', EventDetailsView.as_view(), name='details_event'),
    path('<int:pk>/', EventUpdateView.as_view(), name='update_event'),
    path('<int:pk>/', EventDeleteView.as_view(), name='delete_event'),
]
