
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('submit_response/', views.submit_response, name='submit_response'),
   
    # Other URL patterns
]
