from django.urls import path
from .views import *

urlpatterns = [
    path('movie_api/', movie_api ),
    path('actor_api/', actor_api),
    path('movie_detail/<slug:slug>/', movie_detail_view),
    path('ism_api/', ism_api)
]
