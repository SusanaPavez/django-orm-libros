from django.shortcuts import render, redirect
from books_authors_app.models import * # importas todo, igual que cuando haces shell




def index(request):
    if request.method == 'GET':
        context = {
            'books': Book.objects.all(),
        }
        return render(request, 'index.html', context)

    if request.method == 'POST':
        print(request.POST) # Envias formulario y luego redirige

        titulo = request.POST['title'] #ojo con esto de repetir nombres de variables y todo eso
        descripcion = request.POST['description']

        books = Book.objects.create(
            title = titulo, 
            description = descripcion
            )
        return redirect("/") # redirige a la página en modo GET




def author(request): # Esto es para crear y ver autores
    if request.method == 'GET':
        context = {
            'autor': Author.objects.all(),
        }
        return render(request, 'authors.html', context)

    if request.method == 'POST':
        print(request.POST) # Envias formulario y luego redirige

        nombre = request.POST['first_name'] #ojo con esto de repetir nombres de variables y todo eso
        apellido = request.POST['last_name']

        autor = Author.objects.create(
            first_name = nombre, 
            last_name = apellido
            )
        return redirect("/authors.html") # redirige a la página en modo GET




def authors(request): # Esto es para crear y ver autores
    if request.method == 'GET':
        context = {
            'autor': Author.objects.all(),
        }
        return render(request, 'authors.html', context)

    if request.method == 'POST':
        print(request.POST) # Envias formulario y luego redirige

        nombre = request.POST['first_name'] #ojo con esto de repetir nombres de variables y todo eso
        apellido = request.POST['last_name']

        autor = Author.objects.create(
            first_name = nombre, 
            last_name = apellido
            )
        return redirect("/authors.html") # redirige a la página en modo GET




def book(request, id):

    libro = Book.objects.get(id=id) # aquí estoy creando la variable en base al ID de Books

    if request.method == 'GET':
        context = {
            'book' : libro,
            'autor' : Author.objects.all() # aquí estoy formando los autores.
        }
        return render(request, 'book.html', context) # aquí se va a la página de libros.