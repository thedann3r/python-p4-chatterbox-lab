from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
from flask_migrate import Migrate

from models import db, Message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)

db.init_app(app)

@app.route('/messages')
def messages():
    messages = Message.query.all()
    return jsonify([message.to_dict() for message in messages])

@app.route('/messages/<int:id>', methods = ['PATCH'])
def messages_by_id(id):
    data = request.get_json()
    message = Message.query.get(id)

    if not message:
        return jsonify({'error' : 'the message was not found'}), 404
    

    if 'body' in data:
        message.body = data['body']
    if 'username' in data:
        message.username = data['username']
    if 'created_at' in data:
        message.created_at = data['created_at']
    if 'updated_at' in data:
        message.updated_at = data['updated_at']
    db.session.commit()
    return jsonify(message.to_dict()), 200

@app.route('/messages', methods=['POST'])
def new_messages():
    data = request.get_json()

    body = data['body']
    username = data['username']
    
    if not body or not username:
        return jsonify({'error': 'Both are required'}), 400
    
    new_message = Message(body=body, username=username)
    db.session.add(new_message)
    db.session.commit()

    return jsonify(new_message.to_dict()), 201

@app.route('/messages/<int:id>', methods=['DELETE'])
def delete_messages(id):
    message = Message.query.get(id)
    if not message:
        return jsonify({'error' : 'mesage not found'}), 404
    db.session.delete(message)
    db.session.commit()
    return jsonify({'message' : 'message deleted successfully'}), 200

if __name__ == '__main__':
    app.run(port=5555)
 