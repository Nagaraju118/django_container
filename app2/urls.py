from django.urls import path
from app2.views import*
app_name='raju'
urlpatterns = [
    path('demo2/',demo2,name='demo2'),
]
