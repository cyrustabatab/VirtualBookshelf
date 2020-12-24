from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"

db = SQLAlchemy(app)



class Book(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(250),unique=True,nullable=False)
    author = db.Column(db.String(250),nullable=False)
    rating = db.Column(db.Float,nullable=False)



@app.route('/')
def home():
    
    all_books = Book.query.all()

    return render_template('index.html',books=all_books)


@app.route('/edit',methods=['GET','POST'])
def edit():
    

    _id = request.args.get("_id")
    book = Book.query.get(_id)
    if request.method == 'POST':
        new_rating = request.form['rating']
        book.rating = new_rating
        db.session.commit()
        return redirect(url_for('home'))



    return render_template('edit.html',book=book)

@app.route("/add",methods=['GET','POST'])
def add():

    book_added = False
    if request.method == 'POST':
        name = request.form['name']
        author = request.form['author']
        rating = request.form['rating']

        #all_books.append({'name': name,'author': author,'rating': rating})

        book = Book(title=name,author=author,rating=rating)
        db.session.add(book)
        db.session.commit()


        return redirect(url_for('home'))




    return render_template('add.html',book_added=book_added)


@app.route("/delete")
def delete():

    _id = request.args.get("_id")
    book = Book.query.get(_id)

    db.session.delete(book)
    db.session.commit()

    return redirect(url_for('home'))



if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)

