from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('about_me',views.about_me),
    path('james_consult',views.james_consult),
    path('weather',views.weather),
      
]
