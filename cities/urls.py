from django.urls import path

from cities.views import *

urlpatterns = [
    # path('<int:pk>', home, name='home'),
    # path('', home, name='home'),
    path('', CityListView.as_view(), name='home'),
    path('create/', CityCreateView.as_view(), name='create'),
    path('update/<int:pk>/', CityUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/', CityDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', CityDeleteView.as_view(), name='delete'),
]
