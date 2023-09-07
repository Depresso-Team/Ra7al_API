from django.urls import path
from .views import *


urlpatterns = [
    path('tours/create/', ToursListCreateView.as_view(), name='create-tours-list'),
    path('tours/list/', ToursListView.as_view(), name='list-tours'),
    path('tours/<int:pk>/', ToursListDetailView.as_view(), name='detail-update-delete-tour'),
]
