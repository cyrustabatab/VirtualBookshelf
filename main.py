from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    return render_template('index.html',books=all_books)


@app.route("/add",methods=['GET','POST'])
def add():

    book_added = False
    if request.method == 'POST':
        name = request.form['name']
        author = request.form['author']
        rating = request.form['rating']

        all_books.append({'name': name,'author': author,'rating': rating})
        book_added=True







    return render_template('add.html',book_added=book_added)


if __name__ == "__main__":
    app.run(debug=True)

