
from django.urls import path
from . import views
urlpatterns = [
    path('',views. random_joke,name="random_joke"),
    path('jokes2/',views. random_joke2,name="random_joke2"),
    path('jokes2/',views. random_joke2,name="random_joke2"),
    path('quote/',views.quote_OfThe_Day,name="quote_OfThe_Day"),
    
    
]
