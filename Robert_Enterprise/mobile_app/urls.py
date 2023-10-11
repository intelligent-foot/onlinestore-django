from django.urls import path
from mobile_app import views

urlpatterns = [
    path('',views.home,name='home')
]
