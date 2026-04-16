from fastapi import Body,FastAPI

app=FastAPI()

BOOKS=[
    {'title':'Title One','author':'Author One','category':'science'},
    {'title':'Title Two','author':'Author Two','category':'science'},
    {'title':'Title Three','author':'Author Three','category':'history'},
    {'title':'Title Four','author':'Author Four','category':'math'},
    {'title':'Title Five','author':'Author Five','category':'math'},
    {'title':'Title Six','author':'Author Two','category':'math'},
    ]

# Swagger UI used to see all API endpoints and also there responses
# Get is used to Read data
@app.get('/')
async def first_api():
    return {'message':'Hello Eric!'}

@app.get('/books')
async def read_all_books():
    return BOOKS


# Path Parameters are request parameters attached to URL 
@app.get('/book/mybook')
async def read_all_books():
    return {'book title':'My favourite Book!'}

@app.get('/books/{book_title}')
async def read_book(book_title:str):
    for book in BOOKS:
        if book.get('title').casefold()==book_title.casefold():
            return book

# Dynamic parameters are values in API that are not fixed and are provided at runtime
@app.get('/books/title/{dynamic_param}')
async def read_all(dynamic_param:str): 
    return {'dynamic_param':dynamic_param}

# Order in FastAPI matters since if we define Dynamic one before then all others will be consider as dynamic itself
# Therefore, static and small apis should be kept first than dynamic ones 
# In URL %20 signifies Space

# Query parameter are request parameters attached after '?'
# Ex: 127.0.0.1:8000/books/?category=math

@app.get('/books/')
async def read_category_by_query(category:str):
    books_to_return=[]
    for book in BOOKS:
        if book.get('category').casefold()==category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get('/books/{book_author}/')
async def read_category_by_query(book_author:str,category:str):
    books_to_return=[]
    for book in BOOKS:
        if book.get('author').casefold()==book_author.casefold() and book.get('category').casefold()==category.casefold():
            books_to_return.append(book)
    return books_to_return

# GET cannot have a Body()
# Post is used to create data
@app.post('/books/create_book')
async def create_book(new_book=Body()):
    BOOKS.append(new_book)

# Put used to update data 
@app.put('/books/update_book')
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold()==updated_book.get('title').casefold():
            BOOKS[i]=updated_book

# Delete used to delete data
@app.delete('/books/delete_book/{book_title}')
async def delete_book(book_title:str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold()==book_title.casefold():
            BOOKS.pop(i)
            break

@app.get('/books/author/{book_author}')
async def get_books(book_author:str):
    books_authors=[]
    for book in BOOKS:
        if book.get('author').casefold()==book_author.casefold():
            books_authors.append(book)
    return books_authors
 