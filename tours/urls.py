from django.urls import path
from .views import *


urlpatterns = [
    path('tours/create/', ToursListCreateView.as_view(), name='create-tours-list'),
    path('tours/list/', ToursListView.as_view(), name='list-tours'),
    path('tours/<int:pk>/', ToursListDetailView.as_view(), name='detail-update-delete-tour'),
    path('best_tours/', HighestRateByState.as_view(), name="HighestRateByState"),
    path('save-tour/', SaveTourView.as_view(), name='save-tour'),
    path('saved-tours/', SavedToursListView.as_view(), name='saved-tour-list'),
    path('create-tour/', ToursListCreateView.as_view(), name='create-tour'),
    path('reviews/create/', CreateReviewView.as_view(), name='create_review'),
]
