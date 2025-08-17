from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

db = [{"purchase_id": 1, "item_id": 1, "date": 10, "quantity":3},
       {"purchase_id": 2, "item_id": 2, "date": 20, "quantity":4},
       {"purchase_id": 3, "item_id": 3, "date": 30, "quantity":5}]

class PurchaseItem(BaseModel):
    purchase_id: int
    item_id: int
    date: int
    quantity: int = 1
    remarks: Optional[str] = None

@app.get("/purchase/items")
def read_purchase_items():
    if len(db) == 0:
        return {"error": "No items found"}  
    return db
    
@app.get("/purchase/items/{purchase_id}")
def read_purchase_item(purchase_id: int):
    for purchase_item in db:
        if item["purchase_id"] == purchase_id:
            return purchase_item
    return {"error": "Item not found"}

@app.post("/purchase/items")
def create_purchase_item(purchase_item: PurchaseItem):    
    db.append(purchase_item.dict())
    return {"message": "Purchase Item added successfully", "Purchase item": purchase_item}

@app.put("/purchase/items/{purchase_id}")
def update_purchase_item(purchase_id: int, purchase_item: dict):
    for index, existing_item in enumerate(db):
        if existing_item["purchase_id"] == purchase_id:
            db[index] = purchase_item
            return {"message": "Purchase Item updated successfully", "item": purchase_item}
    return {"error": "Item not found"}

@app.delete("/purchase/items/{purchase_id}")
def delete_item(purchase_id: int):
    for index, purchase_item in enumerate(db):
        if purchase_item["purchase_id"] == purchase_id:
            del db[index]
            return {"message": "Purchase Item deleted successfully"}
    return {"error": "Purchase Item not found"}

@app.get("/purchase/items_sum/count")
def count_purchase_items():
    return {"count": len(db)}

@app.get("/purchase/items_sum/total_quantity")
def total_quantity():
    total = sum(item["quantity"] for item in db)
    return {"total_quantity": total}

