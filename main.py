# main.py
from fastapi import FastAPI, HTTPException
from typing import List
import os
from pydantic import BaseModel
from database import Cliente, Item, drop_cliente_table, create_cliente_table, insert_cliente, drop_item_table, create_item_table, insert_item, get_all_clientes, get_all_items, close_connection, create_initial_data

ENVIRONMENT = os.getenv("ENVIRONMENT", "prueba")
PRODUCTION = os.getenv("PRODUCTION", "produccion")

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    drop_cliente_table()
    drop_item_table()
    create_cliente_table()
    create_item_table()
    create_initial_data()

@app.on_event("shutdown")
async def shutdown_event():
    close_connection()

@app.get("/clientes/", response_model=List[Cliente], tags=["Clientes"])
def read_clientes(skip: int = 0, limit: int = 10):
    return get_all_clientes(skip=skip, limit=limit)

@app.get("/items/", response_model=List[Item], tags=["Items"])
def read_items(skip: int = 0, limit: int = 10):
    return get_all_items(skip=skip, limit=limit)