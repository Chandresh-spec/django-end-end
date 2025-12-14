from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import BookViewset
from .views import Boooks_views,BookMixinsView
router=DefaultRouter()

router.register(r'boo',BookViewset)
urlpatterns = [
    path('', include(router.urls)),
    path('books/',Boooks_views.as_view()),
    path('book/<int:pk>/',BookMixinsView.as_view())

    
]
