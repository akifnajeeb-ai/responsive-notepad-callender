from flask import Flask, request, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__, static_folder='static')

# SQLite DB stored in the same directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(BASE_DIR, 'notes.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Import models after db init to avoid circular imports
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    due = db.Column(db.DateTime, nullable=True)  # optional due date & time

    def as_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "due": self.due.isoformat() if self.due else None,
        }

@app.before_first_request
def create_tables():
    db.create_all()

# API endpoints
@app.route('/api/notes', methods=['GET'])
def get_notes():
    notes = Note.query.all()
    return jsonify([n.as_dict() for n in notes])

@app.route('/api/notes', methods=['POST'])
def add_note():
    data = request.get_json()
    title = data.get('title', '')
    content = data.get('content', '')
    due_str = data.get('due')
    due = None
    if due_str:
        try:
            from datetime import datetime
            due = datetime.fromisoformat(due_str)
        except ValueError:
            pass  # ignore invalid format
    note = Note(title=title, content=content, due=due)
    db.session.add(note)
    db.session.commit()
    return jsonify(note.as_dict()), 201

@app.route('/api/notes/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    note = Note.query.get_or_404(note_id)
    data = request.get_json()
    note.title = data.get('title', note.title)
    note.content = data.get('content', note.content)
    due_str = data.get('due')
    if due_str is not None:
        try:
            from datetime import datetime
            note.due = datetime.fromisoformat(due_str) if due_str else None
        except ValueError:
            pass  # keep existing if parsing fails
    db.session.commit()
    return jsonify(note.as_dict())

@app.route('/api/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    db.session.delete(note)
    db.session.commit()
    return '', 204

# Serve the frontend
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

