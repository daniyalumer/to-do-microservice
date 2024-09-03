from flask import Flask
from flask_restx import Api
from controllers.todo_controller import todo_ns


app = Flask(__name__)
api=Api(app, version='1.0', title='Todo API', description='A simple Todo API')
api.add_namespace(todo_ns, path='/todos')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)