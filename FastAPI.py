from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Créer l'application FastAPI
app = FastAPI()

# Liste pour stocker les items
items: List["Item"] = []

# Modèle Pydantic pour un item
class Item(BaseModel):
    text: str
    is_done: bool = False

# Route racine
@app.get("/")
def root():
    return {"Hello": "World"}

# Créer un item (POST)
@app.post("/items", response_model=Item)
def create_item(item: Item):
    items.append(item)
    return item

# Obtenir un item spécifique par son index (GET)
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    if 0 <= item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")

# Lister les items avec limite (query parameter)
@app.get("/items/", response_model=List[Item])
def list_items(limit: int = 10):
    return items[0:limit]

# Exemple d'endpoint pour tester une erreur
@app.get("/test-error")
def test_error():
    raise HTTPException(status_code=400, detail="This is a test error")
