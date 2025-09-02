from flask import Flask, jsonify, request

app = Flask(__name__)

# "Banco de dados" em memória
tasks = [
    {"id": 1, "title": "Estudar Python", "done": False},
    {"id": 2, "title": "Construir uma API Flask", "done": False}
]

# Rota inicial
@app.route('/')
def home():
    return jsonify({"message": "Bem-vindo à API de Tarefas!"})

# READ - listar todas as tarefas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# CREATE - adicionar nova tarefa
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = {
        "id": len(tasks) + 1,
        "title": data["title"],
        "done": False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

# UPDATE - atualizar uma tarefa pelo ID
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Tarefa não encontrada"}), 404
    
    data = request.get_json()
    task["title"] = data.get("title", task["title"])
    task["done"] = data.get("done", task["done"])
    return jsonify(task)

# DELETE - excluir uma tarefa pelo ID
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return jsonify({"message": "Tarefa deletada com sucesso"})

if __name__ == '__main__':
    app.run(debug=True)
