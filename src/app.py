from flask import Flask
from flask import jsonify
from flask import request
app = Flask(__name__)
todos = [
  { "label": "My first task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
 
  json_text = jsonify(todos)
  return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    json_text = jsonify(todos)
    print("Incoming request with the following body", request_body)
    return json_text


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    del todos[position]
    json_text = jsonify(todos)
    print("This is the position to delete:", position)
    return json_text



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)