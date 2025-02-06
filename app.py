from flask import Flask, request, jsonify
from pydantic import BaseModel
from flask_pydantic import validate

app = Flask(__name__)

seq = 1
database = []

class UserValidator(BaseModel):
    nome: str
    login: str
    nascimento: str
    senha: str

class GetQueryModel(BaseModel):
    id: int

# LIST
@app.route("/user", methods=["GET"])
def get_user():
    return jsonify(database)

# SELECT
@app.route("/user/view", methods=["GET"])
@validate()
def select_user(query: GetQueryModel):
    for obj in database:
        if obj["id"] == query.id:
            return jsonify(obj)

    return jsonify({"message": "Usuário não localizado"})    

# ADD
@app.route("/user/add", methods=["POST"])
@validate()
def add_user(body: UserValidator):
    global seq
    global database

    
    
    new_user = {
            "id": seq,
            "nome": body.nome,
            "login": body.login,
            "data de nascimento": body.nascimento,
            "senha": body.senha
        }
  
    seq = seq + 1
    database.append(new_user)

    return jsonify({"message": "Novo usuário criado", "user": new_user})

# EDIT
@app.route("/user/edit", methods=["PUT"])
@validate()
def edit_user(query: GetQueryModel):
    global database
    new_user = request.json

    found = False
    for i in range(len(database)):
        if database[i]["id"] == query.id:
            database[i]["nome"] = new_user["nome"]
            database[i]["login"] = new_user["login"]
            database[i]["nascimento"] = new_user["nascimento"]
            database[i]["senha"] = new_user["senha"]
            found = True
            break

    if found:
        return jsonify({"message": "Cadastro atualizado"})
    else:
        return jsonify({"message": "Usuário não localizado"})


# DELETE
@app.route("/user/delete", methods=["DELETE"])
@validate()
def remove_user(query: GetQueryModel):
    global database
    
    found = False 
    for i in range(len(database)):
        if database[i]["id"] == query.id:
            database.pop(i)
            found = True
            break
    
    if found:
        return jsonify({"message": "Usuário removido"}) 
    else:
        return jsonify({"message": "Usuário não localizado"})

if __name__ == "__main__":
    app.run()