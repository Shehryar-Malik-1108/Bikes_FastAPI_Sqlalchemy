from fastapi import Depends, FastAPI, HTTPException
from database import MyDatabase

app = FastAPI(title="Sherry Ke Bikes")
db = MyDatabase()


@app.get("/")
def home():
    return "Welcome to Sherry kay Showroom!!"


@app.get("/Select_Bike")
def select_bike(id: int):
    bike = db.select_bike(id)
    if bike:
        return bike
    else:
        return f"Bike: {id} does not exist!"


@app.get("/All_Bikes")
def get_all_bikes():
    return db.get_all_bikes()


@app.post("/Insert_bike")
def insert_bike(id: int, name: str, cc: int, color: str, price: int):
    result = db.insert_bike(id, name, cc, color, price)
    return result


@app.put("/Update_bike")
def update_bike(id: int, price: int):
    result = db.update_bike(id, price)
    return result


@app.delete("/Delete_bike")
def delete_bike(id: int):
    result = db.delete_bike(id)
    return result

