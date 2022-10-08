from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///borrow.db'
# app.config['SQLALCHEMY_DATABASE_MODIFICATION']= False
db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.String, primary_key=True)
    book = db.Column(db.String, unique=False)
    date = db.Column(db.String, unique=False)


db.create_all()


@app.route('/taken', methods=['POST', 'GET'])
def taken():
    if request.method == 'POST':
        id = request.form.get("roll")
        book = request.form.get('book')
        date = request.form.get('date')
        std = Student(id=id, book=book, date=date)
        db.session.add(std)
        db.session.commit()
    return render_template('taken.html')


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        id = request.form.get('roll')
        book = request.form.get('book')
        Book = Student.query.filter_by(id=id).first()
        db.session.delete(Book)
        db.session.commit()
    return render_template('submission.html')


if __name__ == '__main__':
    app.run(debug=True)
