from django.shortcuts import render
import requests
from .models import Post

# Fetch Posts

def fetch_and_save_posts(request):
    api_url = 'https://jsonplaceholder.typicode.com/posts'


    response = requests.get(api_url)
    posts_data = response.json()

    for post in posts_data:
        Post.objects.create(
            title=post['title'],
            body=post['body']
        )
    
    return render(request, 'api/posts.html', {'posts':posts_data})


# Fetch first 10 photos

def fetch_photos(request):
    api_url = 'https://jsonplaceholder.typicode.com/photos'
    
    response = requests.get(api_url)
    photos = response.json()[:10]

    return render(request, 'api/photos.html', {'photos':photos})