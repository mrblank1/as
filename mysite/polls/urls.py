from django.urls import path

import sys
sys.path.append('/home/ahmadreza/Documents/home/ahmadreza/Documents/Projects/mysite/polls/')
import views
urlpatterns = [
    path('', views.index, name='index'),
]