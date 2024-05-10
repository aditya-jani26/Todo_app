from os import abort
from flask import Flask
from flask_restful import  Api, Resource
from wtforms import * 
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, abort
from app import * 

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
db  = SQLAlchemy(app)

class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200))  # Corrected column type
    summary = db.Column(db.String(500))

with app.app_context():
      db.create_all()
todos = {}

task_post_args = reqparse.RequestParser()
task_post_args.add_argument('task', type=str, required=True, help='No task provided', location='json')
task_post_args.add_argument('summary', type=str, required=True, help='No summary provided', location='json')

task_update_args = reqparse.RequestParser()
task_update_args.add_argument('task', type=str)
task_update_args.add_argument('summary', type=str)

class ToDoList(Resource):
    def get(self):
        return todos

class ToDo(Resource):
    def get(self, todo_id):
        if todo_id in todos:
            return todos[todo_id]
        else:
            abort(404, f'Task with ID {todo_id} not found')

    def post(self, todo_id):
        args = task_post_args.parse_args()
        if todo_id in todos:
            abort(409, 'Task ID already exists')
        todos[todo_id] = {"task": args["task"], "summary": args["summary"]}
        return todos[todo_id], 201

    def put(self, todo_id):
        args = task_update_args.parse_args()

        if todo_id not in todos:
            abort(404, 'Task ID does not exist, cannot be updated')

        if args['task']:
            todos[todo_id]['task'] = args['task']

        if args['summary']:
            todos[todo_id]['summary'] = args['summary']
        return todos[todo_id], 200

api.add_resource(ToDo, '/todo/<int:todo_id>')
api.add_resource(ToDoList, '/todo-list')


if __name__ == '__main__':
   app.run(debug = True)