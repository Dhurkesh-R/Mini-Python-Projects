from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Expense {self.amount} {self.category} {self.date}>'

@app.route('/')
def index():
    expenses = Expense.query.all()
    return render_template('index.html', expenses=expenses)

@app.route('/add', methods=['POST'])
def add_expense():
    amount = request.form.get('amount')
    category = request.form.get('category')
    expense = Expense(amount=amount, category=category)
    db.session.add(expense)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_expense(id):
    expense = Expense.query.get(id)
    db.session.delete(expense)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/api/expenses', methods=['GET'])
def get_expenses():
    expenses = Expense.query.all()
    expenses_list = [{'id': exp.id, 'amount': exp.amount, 'category': exp.category, 'date': exp.date} for exp in expenses]
    return jsonify(expenses_list)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
