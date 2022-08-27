from django.urls import path, include

from .views import SnackListView, SnackDetailView
urlpatterns = [
    path('', SnackListView.as_view(), name = 'snack_list'),
    path('snack/<int:pk>/', SnackDetailView.as_view(), name = 'snack_detail'),
]
