from flask import Flask, request, jsonify

app = Flask(__name__)

seq = 1
database = []

# LIST
@app.route("/user", methods=["GET"])
def get_user():
    return jsonify(database)

@app.route("/user/<int:user_id>", methods=["GET"])
def select_user(user_id):
    for obj in database:
        if obj["id"] == user_id:
            return jsonify(obj)

    return jsonify({"message": "Usuário não localizado"})    

# ADD
@app.route("/user/add", methods=["POST"])
def add_user():
    global seq
    global database

    new_user = request.json
    
    database.append(    
        {
            "id": seq,
            "nome": new_user["nome"],
            "login": new_user["login"],
            "data de nascimento": new_user["nascimento"],
            "senha": new_user["senha"]
        }
    )

    new_user["id"] = seq    
    seq = seq + 1

    return jsonify({"message": "Novo usuário criado", "user": new_user})

# EDIT
@app.route("/user/edit/<int:user_id>", methods=["PUT"])
def edit_user(user_id):
    global database
    new_user = request.json

    found = False
    for i in range(len(database)):
        if database[i]["id"] == user_id:
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
@app.route("/user/delete/<int:user_id>", methods=["DELETE"])
def remove_user(user_id):
    global database
    
    found = False 
    for i in range(len(database)):
        if database[i]["id"] == user_id:
            database.pop(i)
            found = True
            break
    
    if found:
        return jsonify({"message": "Usuário removido"}) 
    else:
        return jsonify({"message": "Usuário não localizado"})

if __name__ == "__main__":
    app.run()