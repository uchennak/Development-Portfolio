from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('show_java',views.show_java),
    path('show_python',views.index),
    path('about_me',views.about_me),
      
]
