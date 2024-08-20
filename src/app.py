from flask import Flask, jsonify, request
app = Flask(__name__)




# Suppose you have your data in the variable named some_data
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]








# ADD NEW METHOD
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)


# GET METHOD
@app.route('/todos', methods=['GET'])
def get_todos():
    todo_list = jsonify(todos)
    return todo_list

# DELETE METHOD
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print(f"This is the position to delete: {position}")
    try:
        removed_item = todos.pop(position)
        return jsonify(todos), 200
    except IndexError:
        return jsonify({"error": "Item not found"}), 404
    
    





# These two lines should always be at the end of your app.py file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)