from django.urls import path

from .views import Boooks_views,BookMixinsView

urlpatterns = [
    path('books/',Boooks_views.as_view()),
    path('book/<int:pk>/',BookMixinsView.as_view())

    
]
