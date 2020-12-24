from flask import Flask
from flask_sqlalchemy import SQLAlchemy
'''
import sqlite3



db = sqlite3.connect("books-collection.db")

cursor = db.cursor()


#cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")


cursor.execute("INSERT INTO books VALUES(2,'Fantastic Beasts','J.K. Rowling', 9)")

db.commit()
'''


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Books(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(250),unique=True,nullable=False)
    author = db.Column(db.String(250),nullable=False)
    rating = db.Column(db.Float,nullable=False)


    def __repr__(self):
        return f"<Book: {self.id}, {self.title}, {self.author},{self.rating}"



db.create_all()


book = Books(id=1,title="Harry Potter",author="J.K. Rowling",rating=9.3)


#book_to_update = Books.query.filter_by(title="Harry Potter").first()
#book_to_update.title = "Harry Potter and the Chamber of Secrets"


book_id = 1 
book_to_delete = Books.query.get(book_id)

print(book_to_delete)







