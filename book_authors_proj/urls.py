from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('', include('books_authors_app.urls')),
]