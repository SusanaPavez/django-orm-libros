from django.shortcuts import render, redirect
from books_authors_app.models import * # importas todo, igual que cuando haces shell




def index(request):
    if request.method == 'GET':
        context = {
            'books': Book.objects.all(),
        }
        return render(request, 'index.html', context)

    # Esto es para agregar un libro a la lista
    if request.method == 'POST':
        # Envias formulario y luego redirige
        print(request.POST) 

        # ojo con esto de repetir nombres de variables
        # y todo eso
        titulo = request.POST['title'] 
        descripcion = request.POST['description']

        books = Book.objects.create(
            title = titulo, 
            description = descripcion
            )
        # redirige a la página (en este caso index) en modo GET
        return redirect("/") 





def authors(request):
    if request.method == 'GET':
        print(authors)
        context = {
            'authors': Author.objects.all(), 
            # esto es crítico porque devuelve la tabla
            # de la base de datos. Cuando hacemos un
            # {% for a in authors %} en el html, nos referiremos
            # a esta tabla que se generará.
        }
        return render(request, 'authors.html', context)

    if request.method == 'POST':
        print(request.POST) # Envía formulario y luego redirige

        nombre = request.POST['name']
        apellido = request.POST['last_name']
        notas = request.POST['notes']

        # Esto añade un nuevo autor. 
        # Tengo que encontrar la forma
        # de evitar añadir campos en blanco
        # pero me da flojera ahora mismo
        new_author = Author.objects.create(
            first_name = nombre, 
            last_name = apellido,
            notes = notas
            )

        # redirige a la página authors en modo GET
        return redirect("/authors") 





# Esto es para mostrar la información de un libro
# y agregar autores

def book(request, id):
    # Aquí estoy creando la variable en base al ID de Books
    # Establezco variables, las cuales
    books = Book.objects.get(id=id)
    authors = Author.objects.all()

    # Esto establece contexto a devolver en la página
    if request.method == 'GET':
        context = {
            'book': books,
            'author': authors

        }
        return render(request, 'book.html', context)


    if request.method == 'POST':
        
        # Esto captura la opción de autor
        author = Author.objects.get(id = request.POST['option'])
        print(author)

        # Esto relaciona la opción de autor con el libro
        books.authors.add(author)


        
        return redirect(f'/book/{id}')





def author(request, id):
    # Aquí estoy creando la variable en base al ID de Books
    # Establezco variables, las cuales
    authors = Author.objects.get(id=id)
    books = Book.objects.all()

    # Esto establece contexto a devolver en la página
    if request.method == 'GET':
        context = {
            'book': books,
            'author': authors

        }
        return render(request, 'author.html', context)


    if request.method == 'POST':
        
        # Esto captura la opción de libro
        book = Book.objects.get(id = request.POST['option'])
        print(book)

        # Esto relaciona la opción de autor con el libro
        authors.books.add(book)


        return redirect(f'/author/{id}')