#//How To Use Pydantic//
#from pydantic import BaseModel

#class User(BaseModel):
#    name: str
 #   email: str
#    account_id: int

#user = User(
    #name = "Salah",
    #email = "salah@gmail.com",
    #account_id = 12345
#)
#print(user.name)    # Salah
#print(user.email)    # salah@gmail.com
#print(user.account_id)    # 12345    
#//Validating Data with Pydantic//
#from pydantic import BaseModel

#class User(BaseModel):
    #name: str
   #email: str
#    account_id: int

# It will fail and show a validation error
#user = User(name = 'Ali', email = 'ali@gmailcom', account_id = 'hello')
#print(user)

#from pydantic import BaseModel, EmailStr

#class User(BaseModel):
   # name: str
    #email: EmailStr     # pip install pydantic[email]
   #account_id: int

# It will fail and show a validation error with email = 'ali'
#user = User(name = 'Ali', email = 'ali', account_id = 1234)
#print(user)

#from pydantic import BaseModel, EmailStr

#class User(BaseModel):
  #  name: str
   ## email: EmailStr
  #  account_id: int

#user = User(name='Ali', email='ali@gmail.com', account_id=1234)
#print(user)

#//Custom Field Validation//
#from pydantic import BaseModel, EmailStr, field_validator

#class User(BaseModel):
 #  name: str
  # email: EmailStr
  # account_id: int

    # Exemple de validation personnalisée
#@field_validator("account_id")
    #def validate_account_id(cls, v):
  #      if v <= 0:
       #    raise ValueError("account_id doit être un entier positif.")
# return v

   # user = User(name="Ali", email="ali@gmail.com", account_id=1234)
#print(user)
# you will get a validation error with account_id = -12


#//JSON Serialization//
from pydantic import BaseModel, EmailStr, field_validator

class User(BaseModel):
    name: str
    email: EmailStr
    account_id: int

    @field_validator("account_id")
    def validate_account_id(cls, v):
        if v <= 0:
            raise ValueError("account_id doit être un entier positif.")
        return v

user = User(name="Ali", email="ali@gmail.com", account_id=1234)

# Convertir le modèle en JSON
user_json_str = user.model_dump_json()
# This will return a JSON string representation of the model's data
print(user_json_str)

#//Pydantic vs Dataclasses//
# Python 3.6+
x: int = 0
y: str = "hello"
from dataclasses import dataclass

@dataclass
class User:
    name: str
    email: str
    account_id: int
