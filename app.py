from flask import Flask, request, jsonify

app = Flask(__name__)

books = [
    {
        'id':1,
        "title": "Flask Web Development: Developing Web Applications with Python",
        "author": "Miguel Grinberg",
        "isbn": "978-1491991732",
        
    },
    {
        'id':2,
        "title": "RESTful Web APIs with Flask",
        "author": "Franklin Bien",
        "isbn": "978-1789137485",
       
    },
    {
        'id':3,
        "title": "Flask API Development Cookbook",
        "author": "Shalabh Aggarwal",
        "isbn": "978-1789532019",
        
    },
    {
        'id':4,
        "title": "Building RESTful Python Web Services",
        "author": "Gaston C. Hillar",
        "isbn": "978-1786462251",
        
    }
]

@app.route('/')
def index():
    return 'Home page'
@app.route('/books',methods=['GET', "POST"])
def Books():

    if request.method=='GET':
        if len(books)>0:
            return jsonify(books)
        else:
            'Not Found', 404

    if request.method=='POST':
        new_title =request.form['title']
        new_author = request.form['author']
        new_isbn = request.form['isbn']
        iD = books[-1]['id']+1

        new_object={
            'id':iD,
            'title':new_title,
            'author':new_author,
            'isbn':new_isbn
                    }
        books.append(new_object)
        return jsonify(books), 201
@app.route('/books/<int:id>', methods= ['GET','PUT','DELETE'])
def single_book(id):
    if request.method=='GET':
        for book in books:
            if book['id']==id:
                return jsonify(book)
            pass
    if request.method=='PUT':
        for book in books:
            if book['id']==id:
                book['title'] = request.form['title']
                book['author']=request.form['author']
                book['isbn']=request.form['isbn']
                update_book={
                'id': id,
                'title':book['title'],
                'author':book['author'],
                'isbn':book['isbn']
                }
            return jsonify(update_book)
    if request.method=='DELETE':
        for index, book in enumerate(books):
            if book['id']==id:
                books.pop(index)
                return jsonify(books)
    










if __name__=='__main__':
    app.run(debug=True)