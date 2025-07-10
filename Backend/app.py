from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS # Important for frontend/backend communication
import os
import datetime # Import datetime for handling dates/times

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

# Configure SQLite database (this will create a 'todos.db' file in your backend folder)
# Using os.path.abspath and os.path.dirname for robust path handling
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'todos.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Suppress warning
db = SQLAlchemy(app)

# Define the Todo model (what a todo item looks like in our database)
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    order = db.Column(db.Integer, default=0) # For sorting/reordering
    created_at = db.Column(db.DateTime, default=datetime.datetime.now) # Use datetime.datetime.now

    def __repr__(self):
        return f'<Todo {self.id}: {self.text}>'

    # Helper to convert Todo object to a dictionary for JSON responses
    def to_dict(self):
        return {
            'id': self.id,
            'text': self.text,
            'completed': self.completed,
            'order': self.order,
            'created_at': self.created_at.isoformat() # Convert datetime to ISO format string
        }

# Create database tables (run this once when the app starts)
with app.app_context():
    db.create_all()

# --- API Endpoints ---

# GET all todos
@app.route('/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.order_by(Todo.order, Todo.created_at).all()
    return jsonify([todo.to_dict() for todo in todos])

# POST a new todo
@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'Missing todo text'}), 400

    # Assign a simple order to new todos (last in list)
    max_order = db.session.query(db.func.max(Todo.order)).scalar()
    new_order = (max_order + 1) if max_order is not None else 0

    new_todo = Todo(text=data['text'], order=new_order)
    db.session.add(new_todo)
    db.session.commit()
    return jsonify(new_todo.to_dict()), 201 # Return the newly created todo

# PUT/PATCH to update a todo (e.g., mark as complete, change text, update order)
@app.route('/todos/<int:todo_id>', methods=['PUT', 'PATCH'])
def update_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    data = request.get_json()

    if 'text' in data:
        todo.text = data['text']
    if 'completed' in data:
        todo.completed = data['completed']
    if 'order' in data:
        todo.order = data['order']

    db.session.commit()
    return jsonify(todo.to_dict())

# DELETE a todo
@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return jsonify({'message': 'Todo deleted successfully'})

# DELETE all completed todos
@app.route('/todos/clear-completed', methods=['DELETE'])
def clear_completed_todos():
    Todo.query.filter_by(completed=True).delete()
    db.session.commit()
    return jsonify({'message': 'Completed todos cleared'})

# This runs the Flask development server
if __name__ == '__main__':
    app.run(debug=True, port=5000) # Run on port 5000, debug mode for auto-reloading
