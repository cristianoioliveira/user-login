from app import db

class User(db.Model):
    id = db.Column(db.String, primary_key=True)
    nome = db.Column(db.String(128))
    nascimento = db.Column(db.String(10))
    senha = db.Column(db.String(255))

    def __repr__(self):
        str = "<User {} {}>".format(self.id, self.nome)
        return str

    def to_dict(self):
        obj = {
            "id": self.id,
            "nome": self.nome,
            "nascimento": self.nascimento,
        }

        return obj