from django.urls import path
from .views import customer
urlpatterns = [
    path('customer/',customer.as_view())
]
