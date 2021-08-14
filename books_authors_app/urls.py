from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('book/<int:id>', views.book), # especifico path para libros, usando ID
    path('authors', views.authors), # especifico path para autores en general
    path('author/<int:id>', views.author), # especifico path para autores usando ID
]
