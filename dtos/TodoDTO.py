from flask_restx import Namespace, fields

class ToDoDTO:
    api = Namespace(name='todos', description="todo operations")
    todo_model = api.model('Todo', {
        'id': fields.String(readOnly=True, description='unique identifier'),
        'description': fields.String(required=True, description='description of todo item'),
        'date_created': fields.String(readOnly=True, description='date item created'),
        'date_updated': fields.String(readOnly=True, description='date item updated'),
        'date_completed': fields.String(description='date item marked as completed'),
        'completed': fields.Boolean(description='completion status of todo item')
    })