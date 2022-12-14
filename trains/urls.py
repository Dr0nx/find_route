from django.urls import path

from trains.views import *

urlpatterns = [
    # path('<int:pk>', home, name='home'),
    # path('', home, name='home'),
    path('', TrainListView.as_view(), name='home'),
    path('create/', TrainCreateView.as_view(), name='create'),
    path('update/<int:pk>/', TrainUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/', TrainDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', TrainDeleteView.as_view(), name='delete'),
]
