
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('delete/<CityName>/',views.delete_city,name='delete_city'),
]
