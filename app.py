from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def connection_database():
    conn=None
    try:
        conn=sqlite3.connect('books.sqlite')
    except sqlite3.error as e:
        print(e)
    return conn

@app.route('/')
def index():
    return 'Home page'
@app.route('/books',methods=['GET', "POST"])
def Books():
    conn=connection_database()
    cursor=conn.cursor()

    if request.method=='GET':
        # make a query to the database
        cursor=conn.execute("SELECT * FROM Books")
        books = [
            dict(id =row[0], title=row[1], author=row[2])
            for row in cursor.fetchall()
        ]
        return jsonify(books)
    if request.method=='POST':
        new_title =request.form['title']
        new_author = request.form['author']

        #insert into the table
        insert_query="INSERT INTO BOOKS(Title, Author) VALUES(?,?)"
        cursor.execute(insert_query,(new_title,new_author))
        conn.commit()
        return jsonify({"message":"Book added successfully"}),201

@app.route('/books/<int:id>', methods= ['GET','PUT','DELETE'])
def single_book(id):
    conn=connection_database()
    cursor=conn.cursor()
    if request.method=='GET':
        cursor.execute("SELECT * from Books WHERE id= ?", (id, ))
        book = cursor.fetchone()
        return jsonify(book=dict(id=book[0], title=book[1],author=book[2]))
    if request.method=='PUT':
        cursor.execute('SELECT * FROM BOOKS WHERE Id= ?',(id, ))
        data_old=cursor.fetchone()
        if not data_old:
            return jsonify({"error": "Book not found!"}),404
        new_title =request.form['title']
        new_author = request.form['author']
        update_query='UPDATE BOOKS SET title=?, author=? where id =?'
        cursor.execute(update_query,(new_title,new_author,id))
        conn.commit()
        return jsonify({"message":"The book has been updated succesfully."})
    if request.method=='DELETE':
        cursor.execute('DELETE FROM BOOKS WHERE Id =?',(id,))
        conn.commit()
        return jsonify({"message":"The book has been deleted successfully."})

if __name__=='__main__':
    app.run(debug=True)
