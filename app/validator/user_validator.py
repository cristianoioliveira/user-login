from flask_pydantic import BaseModel

class UserValidatorRequestBody(BaseModel):
    nome: str
    nascimento: str
    senha: str

class UserValidatorRequestQuery(BaseModel):
    id: int