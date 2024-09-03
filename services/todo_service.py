from datetime import datetime
import hashlib


class TodoService:
    def __init__(self):
        self.todo_list=[]

    def generate_hash(self,description):
        return hashlib.md5(description.encode("utf-8")).hexdigest()

    def get_current_time(self):
        return str(datetime.now())[:-7]

    def get_list(self):
        return self.todo_list, 200

    def create_update_list(self, data):
        description=data.get('description')
        id=data.get('id',None)
        completed=data.get('completed',False)


        # mark as completed
        if completed:
            for todo in self.todo_list:
                if todo["id"] == id:
                    if todo["completed"]:
                        return {"message": "Item is already marked as completed"}, 400
                    todo["completed"] = True
                    todo["date_completed"] = self.get_current_time()
                    return {"message": "Item marked as completed", "todo": todo}, 200
            return {"error": "Todo item not found"}, 404


        # update item
        if id:
            for todo in self.todo_list:
                if id == todo["id"]:
                    todo["id"] = self.generate_hash(description)
                    todo["description"] = description
                    todo["date_updated"] = self.get_current_time()
                    return {'message': f'Item {id} updated successfully', 'todo': todo}, 200
            return {"error": "Todo item not found"}, 404

        # create item
        else:
            todo_id = self.generate_hash(description)
            for todo in self.todo_list:
                if todo["id"] == todo_id:
                    return {"error": "Item with the same description already exists"}, 400

            new_todo_item = {
                "id": todo_id,
                "description": description,
                "date_created": self.get_current_time(),
                "date_updated": self.get_current_time(),
                "date_completed": None,
                "completed": False,
            }
            self.todo_list.append(new_todo_item)
            return {'message': 'New item created in to-do list', 'todo': new_todo_item}, 201


