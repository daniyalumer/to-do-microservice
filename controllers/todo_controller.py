from services.todo_service import TodoService
from dtos.TodoDTO import ToDoDTO
from flask_restx import Resource
from flask import request


todo_ns=ToDoDTO.api
todo_model=ToDoDTO.todo_model
service=TodoService()

@todo_ns.route('/')
class TodoListResource(Resource):
    @todo_ns.marshal_list_with(todo_model, envelope='todo_list')
    def get(self):
        return service.get_list()


    @todo_ns.expect(todo_model)
    @todo_ns.response(201, 'To-Do item created, updated or completed')
    @todo_ns.response(400, 'Bad Request')
    def post(self):
        request_data=request.json
        service.create_update_list(request_data)
        

