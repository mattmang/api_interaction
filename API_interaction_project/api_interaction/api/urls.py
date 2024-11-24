from django.urls import path
from .import views

urlpatterns = [
    path('fetch-posts/', views.fetch_and_save_posts, name='fetch_and_save_posts'),
    path('photos/', views.fetch_photos, name='fetch_photos'),
]