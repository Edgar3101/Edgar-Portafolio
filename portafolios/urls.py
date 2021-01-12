from django.urls import path
from . import views
urlpatterns=[
    path('', views.home, name="home"),
    path('my_recent_work/', views.my_recent_work, name="my_recent_work"),
    path('about_me/', views.about_me, name="about_me"),
    path('contacts/', views.contacts, name="contacts"),
]