from django.urls import path
from .views import customer,RegistrationViews,Login_View
from . import views
urlpatterns = [
    path("",views.home,name="home"),
    path('customer/',customer.as_view()),
    path('register/',RegistrationViews.as_view()),
    path('login/',Login_View.as_view())

]
