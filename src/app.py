from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista global de tareas
todos = [
    { "label": "My first task", "done": False }
]

# GET /todos - Devuelve todas las tareas
@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

# POST /todos - Añade una nueva tarea a la lista
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)

# DELETE /todos/<position> - Elimina una tarea por posición
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)

    # Eliminar la tarea en la posición especificada
    if position < len(todos):
        todos.pop(position)

    # Retornar la lista actualizada
    return jsonify(todos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
