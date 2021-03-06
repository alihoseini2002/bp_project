from django.urls import path
from .views import asli,tamarin,videoha
urlpatterns = [
    path('',asli),
    path('tamarin',tamarin,name='ostad_tamarin'),
    path('videoha',videoha,name='ostad\'s videos')
]